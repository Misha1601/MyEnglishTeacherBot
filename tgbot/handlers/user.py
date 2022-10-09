from aiogram import types
from bot import dp, test


@dp.message_handler(commands=["user"])
async def user_start(message: types.Message):
    chat_id = message.chat.id
    await message.answer(f"Hello, user! id {chat_id}")
    await test()
