import datetime

from colour import Color
from cue_csgo.helpers import color_gradient


class BaseRender(object):
    require_color_info = False

    def __init__(self, keyboard, settings, require_color_info=None):
        self.keyboard = keyboard
        self.settings = settings
        if require_color_info is not None:
            self.require_color_info = require_color_info

    def render(self, game_state):
        raise NotImplementedError


class BackgroundRender(BaseRender):
    def render(self, game_state):
        team = game_state["player"]["team"]
        if team == "CT":
            background_color = Color(self.settings["ct_color"])
        if team == "T":
            background_color = Color(self.settings["t_color"])
        for x in self.keyboard.all_leds:
            yield x, background_color


class HpRender(BaseRender):
    def render(self, game_state):
        hp = game_state["player"]["state"]["health"]
        for x in range(20):
            if x < hp//5:
                yield self.keyboard.hp_bars[x], Color("red")


class WeaponRender(BaseRender):
    def render(self, game_state):
        active_color = Color("#00FF00")
        empty_clip_color = Color("#FF0000")

        weapons = game_state["player"]["weapons"]

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


class BombRender(BaseRender):
    def __init__(self, *args, **kwargs):
        super(BombRender, self).__init__(*args, **kwargs)
        self.beep_till = None
        self.sleep_till = None
        self.bomb_timer = None

    def _blink_timeout(self, sec):
        beep_distance_start = 0.83
        beep_distance_end = 0.05
        return beep_distance_start - (sec / (((self.settings["explode_time"] - 1) / beep_distance_start) + beep_distance_end))

    def render(self, game_state):
        now = datetime.datetime.now()

        if self.bomb_timer is None:
            try:
                assert game_state["round"]["bomb"] == "planted"  # Check if bomb is planted
                self.bomb_timer = datetime.datetime.now()
            except (KeyError, AssertionError):
                pass
        else:
            try:
                assert game_state["round"]["bomb"] == "planted"  # Check if bomb still is planted, else stop

                # noinspection PyTypeChecker
                if (now-self.bomb_timer).total_seconds() > self.settings["explode_time"] - 2.3:  # if there is under one second left, display yellowish
                    for x in self.keyboard.keypad:
                        yield x, Color("#AEC187")
                else:
                    if self.beep_till is not None:
                        if self.beep_till < now:
                            self.beep_till = None
                            time_out = self._blink_timeout((now - self.bomb_timer).total_seconds())
                            self.sleep_till = now + datetime.timedelta(seconds=time_out)
                        else:
                            for x in self.keyboard.keypad:
                                yield x, Color("Red")
                    elif self.sleep_till is not None:
                        if self.sleep_till < now:
                            self.sleep_till = None
                            self.beep_till = now + datetime.timedelta(seconds=0.135)  # Beep length ~ 0.135-0.140
                    else:
                        self.beep_till = now + datetime.timedelta(seconds=0.135)  # Beep length ~ 0.135-0.140

            except (KeyError, AssertionError):
                self.bomb_timer = None
                self.sleep_till = None
                self.beep_till = None


class FlashbangRender(BaseRender):
    require_color_info = True

    def render(self, game_state, keyboard_color=None):
        flashed_value = int(game_state["player"]["state"]["flashed"])

        if self.settings["gradient"]:
            for key, org_color in keyboard_color.items():
                if flashed_value > 250:
                    yield key, Color("white")  # Removes redundant calculations
                elif flashed_value > 10:
                    yield key, color_gradient(org_color.hex, "white", 16)[flashed_value//16]
        else:
            for key, org_color in keyboard_color.items():
                if flashed_value > 50:
                    yield key, Color("white")