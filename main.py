import asyncio
import logging
from aiogram import Bot, Dispatcher, executor #, types
from bot.config import load_config
from bot import data
from app import db


logging.basicConfig(level=logging.INFO)

# Загружаем из .env настройки, шаблон настроек в .env_shablon
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp = Dispatcher(bot)
db = db.Database()

try:
    db.create_table_message()
except:
    pass

if __name__=="__main__":
    from bot.handlers import dp
    # from bot.handlers_menu import dp # События на нажатия меню
    # from bot.handlers_user import dp
    # from bot.handlers_echo import dp

    loop = asyncio.get_event_loop()
    loop.create_task(data.napominanie())
    executor.start_polling(dp, skip_updates=True)
