from aiogram import types
from bot import dp

@dp.message_handler()
async def bot_echo(message: types.Message):
    text = [
        "Эхо без состояния.",
        "Сообщение:",
        message.text
    ]

    await message.answer('\n'.join(text))
    # await message.reply('\n'.join(text))
