import logging

from telebot import types

from core.misc import bot

logger = logging.getLogger(__name__)


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    logger.info('%s accessed start command', message.from_user.first_name)
    bot.send_message(message.chat.id, 'Welcome!')


@bot.message_handler(commands=['ping'])
def ping(message: types.Message):
    logger.info('%s accessed ping command', message.from_user.id)
    bot.send_message(message.chat.id, 'Pong!')
