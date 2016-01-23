import logging

from cue_csgo.gui import start_app


def main():
    try:
        start_app()
    except Exception:
        logging.exception()

if __name__ == '__main__':
    main()
