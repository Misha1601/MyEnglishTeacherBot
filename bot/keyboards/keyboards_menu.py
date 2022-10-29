from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# from bot import dp

# клавиатура меню
def buttons_menu():
    keys_menu = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Потренеруемся ещё"),
            KeyboardButton(text="Статистика")
        ]#,
        # [
        #     KeyboardButton(text="🛒 Мои заказы"),
        #     KeyboardButton(text="📢 Новости")
        # ],
        # [
        #     KeyboardButton(text="🔧 Настройки"),
        #     KeyboardButton(text="🚑 Помощь")
        # ]
        ],
    resize_keyboard=True)
    return keys_menu