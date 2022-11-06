import asyncio
import logging
import datetime
from aiogram import Bot, Dispatcher, executor, types
from bot.config import load_config
from bot import handlers
from bot.keyboards import buttons_answer
from app.generator import Generate

# MS = {'471378174':[12, 1667540093]}

logging.basicConfig(level=logging.INFO)

# Загружаем из .env настройки, шаблон настроек в .env_shablon
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp = Dispatcher(bot)


async def proverka(): # необходим ореализовать проверку по ид пользователя
    n = 60
    while True:
        if bool(handlers.MS.keys()) == False:
            print(n)
            await asyncio.sleep(n)
            continue
        min_time_sleep = []
        for key in handlers.MS.keys():
            if not handlers.MS[key][0]:
                continue
            tm = int(datetime.datetime.now().timestamp()) - int(handlers.MS[key][0][0][1].timestamp())
            if tm >= n and len(handlers.MS[key][0]) <= 1:
                msid = await bot.send_message(key, f"{Generate().offer()}\n"
                                "||Tут будет перевод предложения||",
                                parse_mode='MarkdownV2',
                                reply_markup=buttons_answer())
                handlers.MS[key][0].append([msid.message_id, msid.date])
            else:
                min_time_sleep.append(n)

        if min_time_sleep:
            if len(min_time_sleep) > 1:
                sleep_min = n - max(min_time_sleep) #max(tm)
                print(sleep_min)
                await asyncio.sleep(sleep_min)
            if len(min_time_sleep) == 1:
                print(n)
                await asyncio.sleep(n)
        else:
            print(n)
            await asyncio.sleep(n)

if __name__=="__main__":
    from bot.handlers import dp # Команда start
    from bot.handlers_menu import dp # События на нажатия меню
    from bot.handlers_user import dp
    from bot.handlers_echo import dp

    loop = asyncio.get_event_loop()
    loop.create_task(proverka())
    executor.start_polling(dp, skip_updates=True)
