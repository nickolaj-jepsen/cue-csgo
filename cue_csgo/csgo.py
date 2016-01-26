import json
import logging
import sys
import threading
from time import sleep

from cue_csgo.constants import DEFAULT_SETTINGS
from cuepy import CorsairSDK
from flask import Flask, request, jsonify
from cue_csgo.helpers import resource_path, setup_logging

from cue_csgo.renders import *


class Keyboard(object):
    def __init__(self, device):
        self.sdk = CorsairSDK(resource_path("cue_csgo\\resources\\CUESDK.x64_2013.dll"))
        logging.info("Devices found: " + str(self.sdk.device_count()))
        for x in range(1, self.sdk.device_count()+1):
            try:
                logging.info("information for device {}: {}".format(x-1, self.sdk.device_info(x-1)))
            except ValueError:
                logging.info("Error getting information for device: {}".format(x-1))
        self.device = self.sdk.device(device, control=False)
        logging.info("leds for keyboard: {}".format(str(self.device.led_positions()["pLedPosition"])))
        self.device_info = self.device.device_info()
        # TODO: add device specific layouts
        # if self.device_info["model"] == "K70 RGB" and self.device_info["logicalLayout"] == 3:
        self.all_leds = list(self.device.led_positions()["pLedPosition"].keys())
        self.hp_bars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 73, 74, 75, 76, 99, 100, 101, 102]
        self.keypad = [103, 104, 105, 106, 109, 110, 111, 107, 108, 113, 114, 115, 116, 117, 118, 119, 120]

    def set_led(self, key_id, rgb_list):
        self.device.set_led(key_id, rgb_list)

    def set_led_color(self, key_id, color):
        self.set_led(key_id, [int(x*255) for x in color.rgb])


class CueCSGO(object):
    store = {}

    def __init__(self, debug=False, settings=None):

        if settings is not None:
            self.settings = settings
        else:
            try:
                with open("settings.txt") as settings_file:
                    self.settings = json.load(settings_file)
            except FileNotFoundError:
                self.settings = DEFAULT_SETTINGS
                with open('settings.txt', 'w') as settings_file:
                    json.dump(DEFAULT_SETTINGS, settings_file)

        logging.info("Starting keyboard access")
        self.keyboard = Keyboard(self.settings["hardware"]["device_id"])

    def _setup_routes(self, app):
        if self.settings["debug"]:
            @app.route('/')
            def index():
                return jsonify(self.store)

        @app.route('/post', methods=["POST"])
        def post():
            self.store = request.get_json()
            return ''

        return app

    def _setup_renders(self):
        for render in self.settings["renders"]["active"]:

            try:
                settings = self.settings["renders"]["settings"][render]
                logging.info("Adding renderer: " + render + " Found settings")
            except KeyError:
                settings = {}
                logging.info("Adding renderer: " + render + " did not find settings")

            yield getattr(sys.modules[__name__], render)(self.keyboard, settings)

    def start_webserver(self):
        app = Flask(__name__)
        app = self._setup_routes(app)
        app.run(port=43555)

    def main_loop(self):
        renders = list(self._setup_renders())
        previous_dict = {}
        while True:
            if self.store != {}:
                if "team" in self.store["player"]:
                    led_colors = {}
                    for render in renders:
                        if render.require_color_info:
                            for key, color in dict(render.render(self.store, led_colors)).items():
                                led_colors[key] = color
                        else:
                            for key, color in dict(render.render(self.store)).items():
                                led_colors[key] = color

                    if led_colors != previous_dict:  # Don't update keyboard if no change
                        for key, color in led_colors.items():
                            self.keyboard.set_led_color(key, color)
                        previous_dict = led_colors

            sleep(self.settings["update_interval"])

    def start_main_thread(self):
        thread = threading.Thread(target=self.main_loop)
        thread.daemon = True
        thread.start()

    def start(self):
        logging.info("Starting main thread")
        self.start_main_thread()
        logging.info("Starting webserver")
        self.start_webserver()

if __name__ == '__main__':
    try:
        setup_logging()
        cue = CueCSGO()
    except Exception as e:
        logging.exception("An exception has occurred")
