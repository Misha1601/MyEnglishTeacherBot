from aiogram import types
from main import dp

@dp.message_handler()
async def bot_echo(message: types.Message):
    text = ["Этот хэндлер ничего не отправляет"]
    await message.delete()
