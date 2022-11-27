import asyncio
import datetime
from main import bot

async def del_message():
    # смотрим, если запись с таким id, если нет, выходим из функции
    # выгружаем id сообщений и все сообщения удаляем
    # обновляем данные
    pass

async def save_message(message):
    # проверяем, есть ли id в дб
    # если нет, то создаем эту запись
    # добавляем в эту записть id сообщения (хранить в списке или set)
    # сообщений можно передать несколько в кортеже
    pass

async def statistic(statistic):
    # создается при Старте нового пользователя
    # отправка сообщения игры +1,0,0
    # правильный ответ 0,+1,0
    # неправильный ответ 0,0,+1
    # обновляемм данные
    pass

async def state_date(state_date):
    # обновляем статус даты сообщения, необходим для отправки напоминания
    pass

async def trigger(del_message=False,
                  save_message=False,
                  statistic=False,
                  state_date=False):
    """работаем с данными в БД
    - del_message: True - удаляет все предыдущие сообщения
    - save_message: принимает message для сохранения в бд, можно передать
    списком в кортеже.
    - statistic: принимает [0,0,0] где +1 в одной из позиции
                        (1 позиция-сообщение отправлено,
                         2 позиция-получен правильный ответ
                         3 позиция-получен не правильный ответ)
    - state_date - статус даты (1-после старта не начали играть
                                2-игра начата, но нет ответа
                                3-игра начата, получен ответ
                                4-напоминание отправлено, но игра не начата)
    """
    if del_message:
        del_message()
    if save_message:
        save_message()
    if statistic:
        statistic(statistic)
    if state_date:
        state_date(state_date)


if __name__ == '__main__':
    # trigger()
    pass
