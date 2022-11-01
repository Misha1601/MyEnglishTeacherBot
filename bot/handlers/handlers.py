import random
from aiogram import types
from main import dp
from bot.keyboards.keyboards_menu import buttons_menu
from bot.keyboards.keyboards import buttons_answer
from app.generator import Generate
from app.word_collection import verb


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Добро пожаловать в бота для изучения Английского языка\n"
                        "Для получения информации о возможностях бота используйте команду /info\n"
                        "Что бы начать изучение, нажмите /Play",
                        reply_markup=buttons_menu())
    await message.delete()

@dp.message_handler(commands="info")
async def info(message: types.Message):
    await message.answer("В дальнейшем тут будет выведена информация по работе бота, и команда для запуска тестирования") # /start

@dp.message_handler(commands="Play")
async def info(message: types.Message):
    await message.answer(Generate().offer(), reply_markup=buttons_answer())

