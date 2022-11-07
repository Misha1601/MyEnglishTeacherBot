from aiogram import types
from main import dp
from app.data import del_old_messege, save_info_messege
from bot.keyboards import buttons_menu


@dp.message_handler(text="Потренеруемся ещё")
async def vibor_product(message: types.Message):
    mes = await message.answer(f"Тут будет проводиться тренировка ||без учета в статистику или в отдельную статистику||",
                               parse_mode='MarkdownV2',
                               reply_markup=buttons_menu())
    await message.delete()
    await del_old_messege(mes)
    await save_info_messege(mes)

@dp.message_handler(text="Статистика")
async def vibor_product(message: types.Message):
    mes = await message.answer("Информация по статистике, будет позже",
                               reply_markup=buttons_menu())
    await message.delete()
    await del_old_messege(mes)
    await save_info_messege(mes)
