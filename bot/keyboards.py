from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def buttons_menu():
    keys_menu = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Потренеруемся ещё"),
            KeyboardButton(text="Статистика")
        ]
        ],
    resize_keyboard=True)
    return keys_menu

def buttons_answer():
    key_answer = InlineKeyboardMarkup(row_width=2)
    key_answer.insert(InlineKeyboardButton(text="Ответил ✅", callback_data="Yes"))
    key_answer.insert(InlineKeyboardButton(text="Ответил ❌", callback_data="No"))
    return key_answer
