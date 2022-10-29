import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from bot.config import load_config


logging.basicConfig(level=logging.INFO)

# Загружаем из .env настройки, шаблон настроек в .env_shablon
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp = Dispatcher(bot)


if __name__=="__main__":
    from bot.handlers.handlers import dp # Команда start
    from bot.handlers.handlers_menu import dp # События на нажатия меню
    from bot.handlers.admin import dp
    from bot.handlers.user import dp
    from bot.handlers.echo import dp

    executor.start_polling(dp, skip_updates=True)
