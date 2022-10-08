from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from keyboards.callback_datas import view_product, buying_callback, cancellation_callback
from bot import db


# Клавиатура покупки или отмены покупки
def buttons_product(id_product, flag = False):
    key_product = InlineKeyboardMarkup(row_width=2)
    # key_product.insert(InlineKeyboardButton(text="Посмотреть товар", callback_data=view_product.new(id_product=id_product)))
    if flag:
        buying_button = InlineKeyboardButton(text="Купить",
                                               callback_data=buying_callback.new(id_product=id_product))
        key_product.insert(buying_button)
    else:
        cancell_button = InlineKeyboardButton(text="Отменить покупку",
                                               callback_data=cancellation_callback.new(id_product=id_product))
        key_product.insert(cancell_button)
    return key_product
