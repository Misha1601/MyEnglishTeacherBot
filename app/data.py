import asyncio
import datetime
from main import bot
from bot.keyboards import buttons_answer, buttons_no_menu
from app.generator import Generate
from app.translate import Translate

INFO_MESSAGE_ID = {}
INFO_MESSAGE_TIME = {}
STAT = {} # в значении словарь [кол-во play, yes, no]

async def del_old_messege(message):
    if not INFO_MESSAGE_ID or not INFO_MESSAGE_ID[message.chat.id]:
        return None
    element = INFO_MESSAGE_ID[message.chat.id]
    for i in element:
        await bot.delete_message(message.chat.id, i)
        # element.remove(i)
    INFO_MESSAGE_ID[message.chat.id].clear()

async def statistics(message=False, quest=False, yes=False, no=False, stat=False):
    if not STAT.get(message.chat.id):
        STAT[message.chat.id] = [0, 0, 0]
    if message and quest:
        STAT[message.chat.id][0] += 1
    if message and yes:
        STAT[message.chat.id][1] += 1
    if message and no:
        STAT[message.chat.id][2] += 1


async def save_info_messege(message):
    if not INFO_MESSAGE_ID:
        INFO_MESSAGE_ID[message.chat.id] = [message.message_id]

    if not INFO_MESSAGE_TIME:
        INFO_MESSAGE_TIME[message.chat.id] = [message.date]

    if message.message_id not in INFO_MESSAGE_ID[message.chat.id]:
        INFO_MESSAGE_ID[message.chat.id].append(message.message_id)

    if message.date not in INFO_MESSAGE_TIME[message.chat.id]:
        INFO_MESSAGE_TIME[message.chat.id].append(message.date)

async def napominanie(reminder=3600): # необходим ореализовать проверку по ид пользователя
    while True:
        if not INFO_MESSAGE_TIME:
            await asyncio.sleep(reminder)
            continue
        min_time_sleep = []
        for key in INFO_MESSAGE_TIME.keys():
            if not INFO_MESSAGE_TIME[key]:
                continue
            tm = int(datetime.datetime.now().timestamp()) - int(INFO_MESSAGE_TIME[key][-1].timestamp())
            if tm >= reminder:
                word = Generate().offer()
                word_translate = Translate(word=word).perevod()
                mes = await bot.send_message(key, f"{word}\n"
                                f"||{word_translate}||",
                                parse_mode='MarkdownV2',
                                reply_markup=buttons_answer())
                mes1 = await bot.send_message(key, f"В любом обучении главное практика на постоянной основе!",
                                   reply_markup=buttons_no_menu())
                await del_old_messege(mes)
                await save_info_messege(mes)
                await save_info_messege(mes1)
                await statistics(message=mes, quest=True)
                INFO_MESSAGE_TIME[key].clear()
            else:
                min_time_sleep.append(tm)
        if min_time_sleep:
            if len(min_time_sleep) > 1:
                sleep_min = reminder - max(min_time_sleep)
                await asyncio.sleep(sleep_min)
            else:
                await asyncio.sleep(reminder - int(min_time_sleep[0]))
        else:
            await asyncio.sleep(reminder)