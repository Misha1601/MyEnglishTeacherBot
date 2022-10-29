from aiogram import types
from main import dp


@dp.message_handler(commands=["user"])
async def user_start(message: types.Message):
    chat_id = message.chat.id
    await message.answer(f"Hello, user! id {chat_id}")
