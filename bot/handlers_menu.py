from aiogram import types
from main import dp
from app.data import del_old_messege, save_info_messege, statistics
from app import data
from bot.keyboards import buttons_menu
from bot.create_offer_and_send import game


@dp.message_handler(text="Потренеруемся ещё")
async def vibor_product(message: types.Message):
    await game(message=message)

@dp.message_handler(text="Статистика")
async def vibor_product(message: types.Message):
    if data.STAT.get(message.chat.id):
        stat1 = data.STAT[message.chat.id]
        mes = await message.answer(f"Всего задно {stat1[0]} вопроса(ов)\n"
                                   f"Правильно ответили на {stat1[1]} вопроса(ов)\n"
                                   f"Не правильно на {stat1[2]} вопроса(ов)",
                                   reply_markup=buttons_menu())
        await message.delete()
        await del_old_messege(mes)
        await save_info_messege(mes)
    else:
        mes = await message.answer("Вы ещё не ответили ни на один вопрос", reply_markup=buttons_menu())
        await message.delete()
        await del_old_messege(mes)
        await save_info_messege(mes)
