from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from bot.callback_datas import play_collback


def buttons_menu():
    keys_menu = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Потренеруемся ещё"),
            KeyboardButton(text="Статистика")
        ]
        ],
    resize_keyboard=True)
    return keys_menu

def buttons_no_menu():
    keys_menu = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Необходимо выбрать один из вариантов ответа под сообщением!")]],
    resize_keyboard=True)
    return keys_menu

def buttons_answer():
    key_answer = InlineKeyboardMarkup(row_width=2)
    key_answer.insert(InlineKeyboardButton(text="Ответили ✅", callback_data=play_collback.new(yes_or_no="yes")))
    key_answer.insert(InlineKeyboardButton(text="Ответили ❌", callback_data=play_collback.new(yes_or_no="no")))
    return key_answer
