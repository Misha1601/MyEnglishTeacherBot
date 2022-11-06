from ast import Delete
import random
import datetime
from aiogram import types
from main import dp, bot
from bot.keyboards import buttons_answer, buttons_menu
from app.generator import Generate
from app.word_collection import verb

MS = {}
# MS = {471378174: [[623, datetime.datetime(2022, 11, 5, 8, 1, 15)]]}

async def message_del_old_save_new(message):
    if not MS:
        MS[message.chat.id] = [[[message.message_id, message.date]],[],[]]
        return None
    if len(MS.get(message.chat.id)[0]) == 0:
        MS[message.chat.id] = [[[message.message_id, message.date]],[],[]]
        return None
    element = MS.get(message.chat.id)[0]
    # if element:
    for i in element:
        await bot.delete_message(message.chat.id, i[0])
        element.remove(i)
    MS[message.chat.id][0].append([message.message_id, message.date])


@dp.message_handler(commands="start")
async def start(message: types.Message):
    msid = await message.answer("Добро пожаловать в бота для изучения Английского языка\n"
                        "Для получения информации о возможностях бота используйте команду /info\n"
                        "Что бы начать изучение, нажмите /Play",
                        reply_markup=buttons_menu())
    await message.delete()
    await message_del_old_save_new(msid)

@dp.message_handler(commands="info")
async def info(message: types.Message):
    msid = await message.answer("В дальнейшем тут будет выведена информация по работе бота, и команда для запуска тестирования",
                                reply_markup=buttons_menu()) # /start
    await message.delete()
    await message_del_old_save_new(msid)


@dp.message_handler(commands="Play")
async def info(message: types.Message):
    msid = await message.answer(f"{Generate().offer()}\n"
                                "||Tут будет перевод предложения||",
                                parse_mode='MarkdownV2',
                                reply_markup=buttons_answer())
    await message.delete()
    await message_del_old_save_new(msid)
