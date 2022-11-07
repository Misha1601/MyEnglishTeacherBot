import asyncio
import datetime
from main import bot
from bot.keyboards import buttons_answer
from app.generator import Generate

info_message_id = {}
info_message_time = {}

async def del_old_messege(message):
    if not info_message_id or not info_message_id[message.chat.id]:
        return None
    element = info_message_id[message.chat.id]
    print(element)
    for i in element:
        await bot.delete_message(message.chat.id, i)
        # element.remove(i)
    info_message_id[message.chat.id].clear()


async def save_info_messege(message):
    if not info_message_id:
        info_message_id[message.chat.id] = [message.message_id]

    if not info_message_time:
        info_message_time[message.chat.id] = [message.date]

    if message.message_id not in info_message_id[message.chat.id]:
        info_message_id[message.chat.id].append(message.message_id)

    if message.date not in info_message_time[message.chat.id]:
        info_message_time[message.chat.id].append(message.date)

async def napominanie(reminder=20): # необходим ореализовать проверку по ид пользователя
    while True:
        if not info_message_time:
            await asyncio.sleep(reminder)
            continue
        min_time_sleep = []
        for key in info_message_time.keys():
            if not info_message_time[key]:
                continue
            tm = int(datetime.datetime.now().timestamp()) - int(info_message_time[key][-1].timestamp())
            if tm >= reminder:
                msid = await bot.send_message(key, f"{Generate().offer()}\n"
                                f"||Tут будет перевод предложения||",
                                parse_mode='MarkdownV2',
                                reply_markup=buttons_answer())
                save_info_messege(msid)
                info_message_time[key].clear()
            else:
                min_time_sleep.append(tm)

        if min_time_sleep:
            if len(min_time_sleep) > 1:
                sleep_min = reminder - max(min_time_sleep)
                await asyncio.sleep(sleep_min)
            else:
                await asyncio.sleep(int(min_time_sleep[0]))
        else:
            await asyncio.sleep(reminder)