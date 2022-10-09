from aiogram import types
from bot import dp


@dp.message_handler(commands=["admin"]) #, is_admin=True)
async def admin_start(message: types.Message):
    await message.answer("Hello, admin!")


# def register_admin(dp: Dispatcher):
#     dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
