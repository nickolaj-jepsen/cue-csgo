from functools import lru_cache
from time import sleep
import datetime
import threading

from colour import Color
from cuepy import CorsairSDK
from flask import Flask, request, jsonify

from helpers import resource_path, rgb

# SETTINGS
ct_color = Color("#5C7793")
t_color = Color("#C16734")

update_interval = 0.01
flash_bang_gradient = True

bomb_explode_time = 40  # really 40 but because of delay

app = Flask(__name__)
store = {}

sdk = CorsairSDK(resource_path("CUESDK.x64_2013.dll"))
device = sdk.device(0, control=True)

all_leds = list(device.led_positions()["pLedPosition"].keys())
hp_bars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 73, 74, 75, 76, 99, 100, 101, 102]
keypad = [103, 104, 105, 106, 109, 110, 111, 107, 108, 113, 114, 115, 116, 117, 118, 119, 120]

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
            if value > 250:
                yield key, Color("white")  # Removes redundant calculations
            elif value > 10:
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


def blink_timeout(sec):
    beep_distance_start = 0.83
    beep_distance_end = 0.05
    return beep_distance_start - (sec / (((bomb_explode_time - 1) / beep_distance_start) + beep_distance_end))


beep_till = None
sleep_till = None


def bomb_render(bomb_timer):
    global beep_till
    global sleep_till
    now = datetime.datetime.now()

    if (now-bomb_timer).total_seconds() > bomb_explode_time - 2.3:  # if there is under one second left, display red
        for x in keypad:
            yield x, Color("#AEC187")
    else:
        if beep_till is not None:
            if beep_till < now:
                beep_till = None
                sleep_till = now + datetime.timedelta(seconds=blink_timeout((now - bomb_timer).total_seconds()))
            else:
                for x in keypad:
                    yield x, Color("Red")
        elif sleep_till is not None:
            if sleep_till < now:
                sleep_till = None
                beep_till = now + datetime.timedelta(seconds=0.135)  # Beep length ~ 0.135-0.140
        else:
            beep_till = now + datetime.timedelta(seconds=0.135)  # Beep length ~ 0.135-0.140


def main():
    previous_dict = {}
    bomb_timer = None
    while True:
        led_colors = {}
        if store != {}:
            if "team" in store["player"]:
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

                if bomb_timer is None:
                    try:
                        assert store["round"]["bomb"] == "planted"  # Check if bomb is planted
                        bomb_timer = datetime.datetime.now()
                    except (KeyError, AssertionError):
                        pass
                else:
                    try:
                        assert store["round"]["bomb"] == "planted"
                        for key, color in dict(bomb_render(bomb_timer)).items():
                            led_colors[key] = color
                    except (KeyError, AssertionError):
                        bomb_timer = None
                        global sleep_till
                        sleep_till = None
                        global beep_till
                        beep_till = None

                for key, color in dict(flashed_render(flashed, led_colors.copy())).items():
                    led_colors[key] = color

                if led_colors != previous_dict:  # Don't update keyboard if no change
                    print("Updating keyboard")
                    for key, color in led_colors.items():
                        device.set_led(key, rgb(color))
                    previous_dict = led_colors

        sleep(update_interval)


@app.route('/')
def index():
    return jsonify(store)


@app.route('/post', methods=["POST"])
def post():
    global store
    store = request.get_json()
    return ''


if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.daemon = True
    thread.start()
    app.run(debug=True)