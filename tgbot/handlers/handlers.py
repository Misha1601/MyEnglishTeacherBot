from aiogram import types
from bot import dp
from tgbot.keyboards.keyboards_menu import buttons_menu


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Добро пожаловать в бота для покупки товаров ручной работы\n"
                        "Для получения информации о возможностях бота используйте команду /info",
                        reply_markup=buttons_menu())

@dp.message_handler(commands="info")
async def info(message: types.Message):
    await message.answer("Чтобы посмотреть товары используйте команду /product \n" # /start
                         "Чтобы посмотреть товар с фото /product1 \n")

