from ast import Delete
import random
from aiogram import types
from main import dp, bot
from bot.keyboards.keyboards_menu import buttons_menu
from bot.keyboards.keyboards import buttons_answer
from app.generator import Generate
from app.word_collection import verb

MS = {}

async def del_mes(message):
    if MS == False:
        MS[message.chat.id] = [message.message_id]
        return None
    if MS.get(message.chat.id) == None:
        MS[message.chat.id] = []
        return None
    element = MS.get(message.chat.id)
    if element:
        for i in element:
            await bot.delete_message(message.chat.id, i)
            element.remove(i)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await del_mes(message)
    msid = await message.answer("Добро пожаловать в бота для изучения Английского языка\n"
                        "Для получения информации о возможностях бота используйте команду /info\n"
                        "Что бы начать изучение, нажмите /Play",
                        reply_markup=buttons_menu())
    MS[msid.chat.id].append(msid.message_id)
    await message.delete()

@dp.message_handler(commands="info")
async def info(message: types.Message):
    await del_mes(message)
    msid = await message.answer("В дальнейшем тут будет выведена информация по работе бота, и команда для запуска тестирования") # /start
    await message.delete()
    MS[msid.chat.id].append(msid.message_id)

@dp.message_handler(commands="Play")
async def info(message: types.Message):
    await del_mes(message)
    msid = await message.answer(Generate().offer(), reply_markup=buttons_answer())
    await message.delete()
    MS[msid.chat.id].append(msid.message_id)
