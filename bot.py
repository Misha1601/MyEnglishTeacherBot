import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from tgbot.config import load_config


logging.basicConfig(level=logging.INFO)

# Загружаем из .env настройки, шаблон настроек в .env_shablon
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp = Dispatcher(bot)

# тестовая функция для проверки отправки нескольких сообщений
async def test():
    for i in range(5):
        text = f"namber {i}"
        await bot.send_message(471378174, text=text)


if __name__=="__main__":
    from tgbot.handlers.handlers import dp # Команда start
    from tgbot.handlers.handlers_menu import dp # События на нажатия меню
    from tgbot.handlers.admin import dp
    from tgbot.handlers.user import dp
    from tgbot.handlers.echo import dp

    executor.start_polling(dp, skip_updates=True)
