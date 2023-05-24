from aiogram import types
from main import dp
from main import db
from bot.data import del_old_messege, save_info_messege, statistics
from bot import data
from bot.keyboards import buttons_menu
from bot.create_offer_and_send import game


@dp.message_handler(text="Потренеруемся ещё")
async def vibor_product(message: types.Message):
    # удаляем сообщение
    await message.delete()
    # Удаляем все сообщения с пометкой удаления
    await del_old_messege(message)
    await game(message)

    # print(message)

@dp.message_handler(text="Статистика")
async def vibor_product(message: types.Message):
    a = False
    stat = db.statistics(id_chat=message.chat.id)
    if any(stat):
        stat1 = [1, 2, 3]
        mes = await message.answer(f"Всего задно {stat[0]} вопроса(ов)\n"
                                   f"Правильно ответили на {stat[1]} вопроса(ов)\n"
                                   f"Не правильно на {stat[2]} вопроса(ов)",
                                   reply_markup=buttons_menu())
        # удаляем сообщение
        await message.delete()
        # Удаляем все сообщения с пометкой удаления
        await del_old_messege(mes)
        # добавляем в БД запись об отправке сообщения, и помечаем его для дальнейшего удаления
        db.add_message(id_chat=mes.chat['id'], id_message=mes['message_id'], delete=1)
    else:
        mes = await message.answer("Вы ещё не ответили ни на один вопрос", reply_markup=buttons_menu())
        # удаляем сообщение
        await message.delete()
        # Удаляем все сообщения с пометкой удаления
        await del_old_messege(mes)
        # добавляем в БД запись об отправке сообщения, и помечаем его для дальнейшего удаления
        db.add_message(id_chat=mes.chat['id'], id_message=mes['message_id'], delete=1)
        # print(mes)
