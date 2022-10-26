import random
from aiogram import types
from bot import dp
from tgbot.keyboards.keyboards_menu import buttons_menu
from app.offer_generator import Offer_g
from app.parts_of_speech.verb import correct


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Добро пожаловать в бота для изучения Английского языка\n"
                        "Для получения информации о возможностях бота используйте команду /info\n"
                        "Что бы начать изучение, нажмите /Play",
                        reply_markup=buttons_menu())

@dp.message_handler(commands="info")
async def info(message: types.Message):
    await message.answer("В дальнейшем тут будет выведена информация по работе бота, и команда для запуска тестирования") # /start

@dp.message_handler(commands="Play")
async def info(message: types.Message):
    word = random.choice(tuple(correct.keys()))
    word1 = Offer_g(word)
    await message.answer("Работа основной логики бота")
    await message.answer(word1.generator())

