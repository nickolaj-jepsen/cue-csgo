import logging

from cue_csgo.gui import start_app
from cue_csgo.helpers import setup_logging


def main():
    try:
        setup_logging(debug=False)
        start_app()
    except Exception:
        logging.exception("")

if __name__ == '__main__':
    main()
