import io
import logging
import os
from zipfile import ZipFile

from telebot import types

from core.misc import bot
from ..utils import is_admin

logger = logging.getLogger(__name__)


@bot.message_handler(func=is_admin, commands=['logs'])
def send_logs(message: types.Message):
    logger.info('sending logs to %s', message.from_user.first_name)

    with io.BytesIO() as file:
        file.name = 'logs.zip'
        with ZipFile(file, 'w') as zip_file:
            for log in os.listdir('./logs/'):
                zip_file.write(f'./logs/{log}')

        file.seek(0)
        bot.send_document(message.chat.id, file)
