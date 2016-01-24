import logging
import os
import platform

import sys
from functools import lru_cache

from colour import Color


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


@lru_cache(maxsize=200)
def color_gradient(org_color, new_color, steps):
    return list(Color(org_color).range_to(Color(new_color), steps))


def setup_logging(debug=False, os_info=True):
    if os.environ.get("CUECSGO_DEBUG") == "1":
        debug = True

    if not debug:
        format_ = '%(asctime)-15s || %(message)s'
        logging.basicConfig(filename="CUE_gamestate.log", format=format_, level=logging.INFO, filemode="w")
        log = logging.getLogger("werkzeug")
        log.setLevel(logging.WARNING)
    else:
        logging.basicConfig(level=logging.INFO)

    if os_info:
        logging.info("Windows platform\t= {}".format(platform.platform()))
        if 'PROGRAMFILES(X86)' in os.environ:
            logging.info("System Arch\t\t= {}".format("64 bit"))
        else:
            logging.info("System Arch\t\t= {}".format("32 bit"))
        logging.info("Python version\t= {}".format(sys.version))
