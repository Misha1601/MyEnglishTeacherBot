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
        if datetime.datetime.now().hour in (21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8):
            await asyncio.sleep(3600)
            continue
        # получаем все id чатов
        all_id_chat = db.select_all_chat()
        # максимальное время засывания для каждого чата
        min_time_sleep = []
        for i in all_id_chat:
            # последнее максимальное время ответа на сообщение
            dt = db.napominanie(id_chat=i[0])
            # разница в секундах с последним обновлением
            rasn_sec = int((datetime.datetime.now() - datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")).total_seconds())
            # если разница больше заданного времени, отправляем сообщение
            if (rasn_sec > reminder):
                # получаем последнюю запись с отправленным словом
                old_word = db.max_date_update(id_chat=i[0])
                # если на него отвечали data_update, то отправляем сообщение
                if old_word[5]:
                    await game(i[0])
                # иначе разница должна быть более 6-и часов, 21600 сек
                else:
                    if int((datetime.datetime.now() - datetime.datetime.strptime(old_word[3], "%Y-%m-%d %H:%M:%S")).total_seconds()) > 21600:
                        await game(i[0])
            # иначе добавляем эту разницу в переменную
            else:
                min_time_sleep.append(rasn_sec)

        # смотрим список с разницей во времени для всех чатов
        if min_time_sleep:
            # если больше одного
            if len(min_time_sleep) > 1:
                # выбираем максимальную разницу во времени, и на него засыпаем, после цикл сбразывается
                sleep_min = reminder - int(max(min_time_sleep))
                await asyncio.sleep(sleep_min)
                continue
            else:
                # аналогично предыдущему, только для одного чата
                await asyncio.sleep(reminder - int(min_time_sleep[0]))
                continue
        else:
            # если нет ни одного чата, засыпаем
            await asyncio.sleep(reminder)

if __name__=="__main__":
    print(datetime.datetime.now().hour)
    if datetime.datetime.now().hour in (21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8):
        print("Yes")
    else:
        print("No")

