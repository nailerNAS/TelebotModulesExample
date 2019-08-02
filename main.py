import logging
import os
from logging import Formatter
from logging.handlers import RotatingFileHandler

import core.misc


def setup_logging():
    if not os.path.exists('./logs/'):
        os.mkdir('./logs/')

    fmt = '[%(levelname)s %(asctime)s %(name)s] : %(message)s'
    logging.basicConfig(format=fmt, level=logging.INFO)

    formatter = Formatter(fmt)

    file_handler = RotatingFileHandler('./logs/bot.log', maxBytes=2000, backupCount=5)
    file_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(file_handler)


def main():
    setup_logging()
    core.misc.start()


if __name__ == '__main__':
    main()
