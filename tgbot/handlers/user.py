from aiogram import Dispatcher
from aiogram.types import Message


async def user_start(message: Message):
    user_id = message.from_user.id
    await message.reply(f"Hello, user! id {user_id}")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
