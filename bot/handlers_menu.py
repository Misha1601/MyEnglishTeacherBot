from aiogram import types
from main import dp
from app.data import del_old_messege, save_info_messege, statistics
from bot.keyboards import buttons_menu, buttons_answer
from app.generator import Generate


@dp.message_handler(text="Потренеруемся ещё")
async def vibor_product(message: types.Message):
    mes = await message.answer(f"{Generate().offer()}\n"
                                "||Tут будет перевод предложения||",
                                parse_mode='MarkdownV2',
                                reply_markup=buttons_answer())
    await message.delete()
    await del_old_messege(mes)
    await save_info_messege(mes)
    await statistics(mes) # реализовать это в отделный параметр статистики

@dp.message_handler(text="Статистика")
async def vibor_product(message: types.Message):
    stat = statistics(message=False, stat=True)
    mes = await message.answer(f"Всего задно {stat[0]} вопросов\n",
                               f"Правильно ответили на {stat[1]} вопросов\n",
                               f"Не правильно на {stat[2]} вопросов\n",
                               reply_markup=buttons_menu())
    await message.delete()
    await del_old_messege(mes)
    await save_info_messege(mes)
