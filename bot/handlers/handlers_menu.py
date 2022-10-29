from aiogram import types
from main import dp


@dp.message_handler(text="Потренеруемся ещё")
async def vibor_product(message: types.Message):
    await message.answer(f"Тут будет проводиться тренировка ||без учета в статистику или в отдельную статистику||", parse_mode='MarkdownV2')

@dp.message_handler(text="Статистика")
async def vibor_product(message: types.Message):
    await message.answer("Информация по статистике, будет позже")
