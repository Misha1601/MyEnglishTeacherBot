from aiogram import types
from aiogram.types import CallbackQuery
from main import dp, bot
from bot.keyboards import buttons_answer, buttons_menu
from app.generator import Generate
from app.data import del_old_messege, save_info_messege, statistics
from bot.callback_datas import play_collback


@dp.message_handler(commands="start")
async def start(message: types.Message):
    msid = await message.answer("Добро пожаловать в бота для изучения Английского языка\n"
                        "Для получения информации о возможностях бота используйте команду /info\n"
                        "Что бы начать изучение, нажмите /Play",
                        reply_markup=buttons_menu())
    await message.delete()
    await del_old_messege(msid)
    await save_info_messege(msid)

@dp.message_handler(commands="info")
async def info(message: types.Message):
    msid = await message.answer("В дальнейшем тут будет выведена информация по работе бота, и команда для запуска тестирования",
                                reply_markup=buttons_menu()) # /start
    await message.delete()
    await del_old_messege(msid)
    await save_info_messege(msid)


@dp.message_handler(commands="Play")
async def info(message: types.Message):
    msid = await message.answer(f"{Generate().offer()}\n"
                                "||Tут будет перевод предложения||",
                                parse_mode='MarkdownV2',
                                reply_markup=buttons_answer())
    await message.delete()
    await del_old_messege(msid)
    await save_info_messege(msid)
    await statistics(msid)

@dp.callback_query_handler(play_collback.filter(yes_or_no="yes"))
async def inline_yes(call: CallbackQuery, callback_data: dict):
    await call.answer()
    press = callback_data.get("yes_or_no")
    msid = await call.message.answer(f"Вы нажали кнопку {press}", reply_markup=buttons_menu())
    await call.message.edit_reply_markup()
    await save_info_messege(msid)
    await statistics(msid, yes=True)

@dp.callback_query_handler(play_collback.filter(yes_or_no="no"))
async def inline_no(call: CallbackQuery, callback_data: dict):
    await call.answer()
    press = callback_data.get("yes_or_no")
    msid = await call.message.answer(f"Вы нажали кнопку {press}", reply_markup=buttons_menu())
    await call.message.edit_reply_markup()
    await save_info_messege(msid)
    await statistics(msid, no=True)