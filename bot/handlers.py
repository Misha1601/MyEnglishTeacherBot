from aiogram import types
from aiogram.types import CallbackQuery
from main import dp
from bot.keyboards import buttons_menu
from bot.create_offer_and_send import game
from bot.data import del_old_messege
from bot.callback_datas import play_collback
from main import db


@dp.message_handler(commands="start")
async def start(message: types.Message):
    msid = await message.answer("Добро пожаловать в бота для изучения Английского языка\n"
                        "Для получения информации о возможностях бота используйте команду /info\n"
                        "Что бы начать изучение, нажмите /Play")
                        # reply_markup=buttons_menu())
    # удаляем сообщение "start"
    await message.delete()
    # Удаляем все сообщения с пометкой удаления
    await del_old_messege(msid)
    # добавляем в БД запись об отправке сообщения, и помечаем его для дальнейшего удаления
    db.add_message(id_chat=msid.chat['id'], id_message=msid['message_id'], delete=1)
    # await save_info_messege(msid)

@dp.message_handler(commands="info")
async def info(message: types.Message):
    msid = await message.answer("В дальнейшем тут будет выведена информация по работе бота, и команда для запуска тестирования\n"
                                "Что бы начать изучение, нажмите /Play")
                                # reply_markup=buttons_menu()) # /start
    # удаляем сообщение "info"
    await message.delete()
    # Удаляем все сообщения с пометкой удаления
    await del_old_messege(msid)
    # добавляем в БД запись об отправке сообщения, и помечаем его для дальнейшего удаления
    db.add_message(id_chat=msid.chat['id'], id_message=msid['message_id'], delete=1)


@dp.message_handler(commands="Play")
async def play(message: types.Message):
    # удаляем сообщение "info"
    await message.delete()
    # Удаляем все сообщения с пометкой удаления
    await del_old_messege(message)
    # запускаем функцию отправки слова
    await game(message)


@dp.callback_query_handler(play_collback.filter(yes_or_no="yes"))
async def inline_yes(call: CallbackQuery, callback_data: dict):
    await call.answer()
    # msid = await call.message.answer(f"Отлично, вы запомнили эти слова и эту конструкцию предложения!",
    #                                  reply_markup=buttons_menu())
    await call.message.edit_reply_markup()

    # Удаляем все сообщения с пометкой удаления
    # await del_old_messege(msid)
    # добавляем в БД запись об отправке сообщения, и помечаем его для дальнейшего удаления
    # db.add_message(id_chat=msid.chat['id'], id_message=msid['message_id'], delete=1)
    # если правильный ответ, помечаем 1
    db.update(id_chat=call.message.chat.id, id_message=call.message.message_id, status=1)
    # await statistics(message=msid, yes=True)

@dp.callback_query_handler(play_collback.filter(yes_or_no="no"))
async def inline_no(call: CallbackQuery, callback_data: dict):
    await call.answer()
    # msid = await call.message.answer(f"Необходимо выучить используемые слова и повторить конструкции предложения",
    #                                  reply_markup=buttons_menu())
    await call.message.edit_reply_markup()

    # Удаляем все сообщения с пометкой удаления
    # await del_old_messege(msid)
    # добавляем в БД запись об отправке сообщения, и помечаем его для дальнейшего удаления
    # db.add_message(id_chat=msid.chat['id'], id_message=msid['message_id'], delete=1)
    # если правильный ответ, помечаем 1
    db.update(id_chat=call.message.chat.id, id_message=call.message.message_id, status=0)
    # await statistics(message=msid, no=True)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# handlers_menu, хундреры отвечающие за меню!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

@dp.message_handler(text="Потренеруемся ещё")
async def vibor_product(message: types.Message):
    # удаляем сообщение
    await message.delete()
    # Удаляем все сообщения с пометкой удаления
    await del_old_messege(message)
    # запускаем функцию отправки слова
    await game(message)


@dp.message_handler(text="Статистика")
async def vibor_product(message: types.Message):
    # запрашиваем в БД все сообщения со словами, получаем кортеж
    stat = db.statistics(id_chat=message.chat.id)
    if any(stat):
        mes = await message.answer(f"Всего задно {stat[0]} вопроса(ов)\n"
                                   f"Правильно ответили на {stat[1]} вопроса(ов)\n"
                                   f"Не правильно на {stat[2]} вопроса(ов)",
                                   reply_markup=buttons_menu())
    else:
        mes = await message.answer("Вы ещё не ответили ни на один вопрос", reply_markup=buttons_menu())

    # удаляем сообщение "Статистика"
    await message.delete()
    # Удаляем все сообщения с пометкой удаления
    await del_old_messege(message)
    # добавляем в БД запись об отправке сообщения, и помечаем его для дальнейшего удаления
    db.add_message(id_chat=mes.chat['id'], id_message=mes['message_id'], delete=1)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# handlers_user, тестовый хэндлер!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

@dp.message_handler(commands=["user"])
async def user_start(message: types.Message):
    mes = message.chat
    n = db.select_all_chat()
    info_message = await message.answer(f"Hello, user! Информация о Вас - {mes}\nВсего пользователей использующих бота - {len(n)}.\n{n}", reply_markup=buttons_menu())
    # Удаляем все сообщения с пометкой удаления
    await del_old_messege(message)
    # удаляем сообщение
    await message.delete()
    # добавляем в БД запись об отправке сообщения, и помечаем его для дальнейшего удаления
    db.add_message(id_chat=info_message.chat['id'], id_message=info_message['message_id'], delete=1)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Хэндлер, должен быть последним, просто удаляет отправленное сообщение!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

@dp.message_handler()
async def bot_echo(message: types.Message):
    # "Этот хэндлер ничего не отправляет"
    await message.delete()