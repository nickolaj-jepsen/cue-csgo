from functools import lru_cache
from flask import Flask, request, jsonify
from colour import Color

from helpers import resource_path
from cuepy import CorsairSDK

# SETTINGS
ct_color = Color("#5C7793")
t_color = Color("#C16734")

flash_bang_gradient = True

app = Flask(__name__)
store = {}

sdk = CorsairSDK(resource_path("CUESDK.x64_2013.dll"))
device = sdk.device(0, control=True)

all_leds = list(device.led_positions()["pLedPosition"].keys())
hp_bars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 73, 74, 75, 76, 99, 100, 101, 102]
rest_of_keys = [x for x in all_leds if x not in hp_bars]


def rgb(color):
    return [int(x*255) for x in color.rgb]


@lru_cache(maxsize=200)
def color_gradient(org_color, new_color, steps):
    return list(Color(org_color).range_to(Color(new_color), steps))


def hp_render(hp):
    for x in range(20):
        if x < hp//5:
            yield hp_bars[x], Color("red")


def flashed_render(value, current_keys):
    if flash_bang_gradient:
        for key, org_color in current_keys.items():
            yield key, color_gradient(org_color.hex, "white", 16)[value//16]
    else:
        for key, org_color in current_keys.items():
            if value > 50:
                yield key, Color("white")


def background_render(team):
    if team == "CT":
        background_color = ct_color
    if team == "T":
        background_color = t_color
    for x in all_leds:
        yield x, background_color


def weapon_render(weapons):
    active_color = Color("#00FF00")
    empty_clip_color = Color("#FF0000")
    for key, weapon in weapons.items():
        try:
            if weapon["type"] == "Knife":
                yield 16, active_color
            if weapon["type"] == "Pistol":
                yield 15, color_gradient(empty_clip_color.hex, active_color.hex, weapon["ammo_clip_max"]+1)[weapon["ammo_clip"]]
            if weapon["type"] in ["Rifle", "Shotgun", "Machine Gun", "Submachine Gun", "SniperRifle"]:
                yield 14, color_gradient(empty_clip_color.hex, active_color.hex, weapon["ammo_clip_max"]+1)[weapon["ammo_clip"]]
            if weapon["type"] == "C4":
                yield 18, active_color
            if weapon["type"] == "Grenade":
                yield 17, active_color
                if weapon["name"] == "weapon_hegrenade":
                    yield 19, active_color
                if weapon["name"] == "weapon_flashbang":
                    yield 20, active_color
                if weapon["name"] == "weapon_smokegrenade":
                    yield 21, active_color
                if weapon["name"] == "weapon_decoy":
                    yield 22, active_color
                if weapon["name"] in ["weapon_molotov", "weapon_incgrenade"]:
                    yield 23, active_color

        except KeyError:
            pass  # Zeus


@app.route('/')
def index():
    return jsonify(store)


@app.route('/post', methods=["POST"])
def post():
    global store
    global device
    global sdk
    store = request.get_json()
    led_colors = {}
    if "team" in store["player"]:
        device.request_control(True)

        team = store["player"]["team"]
        hp = int(store["player"]["state"]["health"])
        weapons = store["player"]["weapons"]
        flashed = int(store["player"]["state"]["flashed"])

        for key, color in dict(background_render(team)).items():
            led_colors[key] = color
        for key, color in dict(hp_render(hp)).items():
            led_colors[key] = color
        for key, color in dict(weapon_render(weapons)).items():
            led_colors[key] = color
        for key, color in dict(flashed_render(flashed, led_colors.copy())).items():
            led_colors[key] = color
        for key, color in led_colors.items():
            device.set_led(key, rgb(color))

    return ''


if __name__ == '__main__':
    app.run(debug=True)
