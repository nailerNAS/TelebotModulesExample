import logging

from telebot import TeleBot

import consts
from .packages import PackageLoader

logger = logging.getLogger(__name__)
bot = TeleBot(consts.TOKEN, skip_pending=True)


def start():
    logging.info('Loading modules')
    PackageLoader().load_package('modules.bot')

    logging.info('Starting polling')
    try:
        bot.polling()
    except KeyboardInterrupt:
        logging.info('Stopping polling')
        bot.stop_polling()
