import asyncio
import datetime
from main import bot
from main import db
from bot.create_offer_and_send import game


async def del_old_messege(message):
    list_del_message = db.select_del_message(id_chat=message.chat['id'])
    for i in list_del_message:
        # print(i[0])
        await bot.delete_message(message.chat.id, message_id=i[0])
        db.update(id_chat=message.chat.id, id_message=i[0], delete=0)

async def napominanie(reminder=1800):
    while True:
        # min_time_sleep = []
        # for key in INFO_MESSAGE_TIME.keys():
        #     tm = int(datetime.datetime.now().timestamp()) - int(INFO_MESSAGE_TIME[key][-1].timestamp())
        #     if tm >= reminder:
        #         from bot.create_offer_and_send import game
        #         await game(key)
        #         INFO_MESSAGE_TIME[key].clear()
        #     else:
        #         min_time_sleep.append(tm)
        # if min_time_sleep:
        #     if len(min_time_sleep) > 1:
        #         sleep_min = reminder - max(min_time_sleep)
        #         await asyncio.sleep(sleep_min)
        #     else:
        #         await asyncio.sleep(reminder - int(min_time_sleep[0]))
        # else:
        #     await asyncio.sleep(reminder)
            # -------------------------------------------------------------------------------------

        # Ищем все чаты со словами
        # пробегаемся по всем чатам ищем максимальную дату
        #     возвращаем дату обновления или отправки для конкретного чата со словом
        # если разница дат больше заданного числа, отправляем сообщение
        all_id_chat = db.select_all_chat()
        min_time_sleep = []
        for i in all_id_chat:
            dt = db.napominanie(id_chat=i[0])
            rasn_sec = int((datetime.datetime.now() - datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")).total_seconds())
            if (rasn_sec > reminder):
                await game(i[0])
            else:
                min_time_sleep.append(rasn_sec)

        if min_time_sleep:
            if len(min_time_sleep) > 1:
                sleep_min = reminder - int(max(min_time_sleep))
                await asyncio.sleep(sleep_min)
                continue
            else:
                await asyncio.sleep(reminder - int(min_time_sleep[0]))
                continue
        else:
            await asyncio.sleep(reminder)

