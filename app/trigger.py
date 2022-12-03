import asyncio
import datetime
# from main import bot


async def del_message():
    # смотрим, если запись с таким id, если нет, выходим из функции
    # выгружаем id сообщений и все сообщения удаляем
    # обновляем данные
    pass


async def save_message(message):
    # проверяем, есть ли id в дб
    # если нет, то создаем эту запись
    # добавляем в эту записть id сообщения (хранить в списке или set)
    # сообщения можно передать несколько в кортеже
    pass

# async def statistic(statistic):
async def statistic_start_play():
    # создается при Старте нового пользователя
    # отправка сообщения игры +1,0,0
    # правильный ответ 0,+1,0
    # неправильный ответ 0,0,+1
    # обновляемм данные
    pass

async def statistic_yes():
    pass

async def statistic_no():
    pass

async def date_start():
    # обновляем статус даты сообщения, необходим для отправки напоминания
    pass

async def date_start_play():
    pass

async def date_answer_yes_or_no():
    pass

async def date_napominanie():
    pass

async def trigger(del_message=False,
                  save_message=False,
                  statistic=False,
                  state_date=False):
    """работаем с данными в БД
    - del_message: True - удаляет все предыдущие сообщения
    - save_message: принимает message для сохранения в бд, можно передать списком в кортеже.
    - statistic_start_play: сообщение с вопросом отправлено
    - statistic_yes: получен правильный ответ на вопрос
    - statistic_no: получен не правильный ответ на вопрос
    - date_start: дата нажатия старта, не перезаписывается
    - date_start_play: сообщение с вопросом отправлено
    - date_answer_yes_or_no: получен правильный или не правильный ответ
    - date_napominanie: напоминание отправлено
    """
    if del_message:
        await del_message()
    if save_message:
        await save_message()
    if statistic_start_play:
        await statistic_start_play()
    if statistic_yes:
        await statistic_yes()
    if statistic_no:
        await statistic_no()
    if date_start:
        await date_start()
    if date_start_play:
        await date_start_play()
    if date_answer_yes_or_no:
        await date_answer_yes_or_no()
    if date_napominanie:
        await date_napominanie()

if __name__=="__main__":
    asyncio.run(trigger())
