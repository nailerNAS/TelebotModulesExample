from telebot.types import Message

import consts


def is_admin(message: Message) -> bool:
    return message.from_user.id in consts.ADMINS
