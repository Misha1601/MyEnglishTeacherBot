from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


bot = Bot(token="5085745854:AAH9eSK7kAnzNFuTXyK_eshs5azG8wiiWY0")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

questions = {
    "вопрос 1": [
        "ответ 1",
        "ответ 2",
        "ответ 3",
    ],
    "вопрос 2": [
        "ответ 1",
        "ответ 2",
        "ответ 3",
    ],
    "вопрос 3": [
        "ответ 1",
        "ответ 2",
        "ответ 3",
    ]
}


class Dialog(StatesGroup):
    name = State()
    victorina = State()


@dp.message_handler(commands="start")
async def start(msg: types.Message):
    await Dialog.name.set()
    await msg.delete()


@dp.message_handler(state=Dialog.name)
async def take_name_and_start_questions(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answers'] = []
        data['cur_question'] = 1
        data['name'] = msg.text

        for i, question in enumerate(questions):
            # тут выводим только первый вопрос
            if i != 0:
                break
            answers = questions[question]
            kb = create_kb(len(answers))
            text = question + "\n"
            for j, answer in enumerate(answers):
                text += f'{j + 1}) {answer} \n'

        await msg.answer(text, reply_markup=kb)

    await Dialog.victorina.set()


# тут должны обрабатываться ответы
@dp.message_handler(state=Dialog.victorina)
async def save_answer(msg: types.Message, state: FSMContext):
    # добавляем ответ в массив
    async with state.proxy() as data:
        data['answers'].append(int(msg.text))

        # ну и выводим некст вопрос
        for i, question in enumerate(questions):
            # выводит только след вопрос
            if i == data['cur_question']:
                kb = create_kb(len(questions[question]))
                text = question + "\n"
                for j, answer in enumerate(questions[question]):
                    text += f'{i}) {answer} \n'
                # ну и чтобы зря не работал for брейкаем его
                break
        # делаем сразу некст вопрос
        data['cur_question'] += 1
    # ну и если вопросы кончились то никакого text ни kb не будет делаем проверку
    if text:
        await msg.answer(text, reply_markup=kb)
    else:
        # собственно если нету то удалаем клавиатуру и пишем что-то
        await msg.answer("конец викторины", reply_markup=ReplyKeyboardRemove())
        # а также в зависимости как вы работаете с стейтом делате или
        await state.finish()
        # или удаляете переменные в стейт ручками по типу
        # del data['answers']
        # и тд... Ну и само собой не забудьте забрать нужные вам данные до их удаление. Тобишь выше но в блоке елс


# создание клавиатуры с ответами 1-2-3 в зависимости от их числа
def create_kb(count: int):
    kb = ReplyKeyboardMarkup()
    for num in range(1, count + 1):
        button = KeyboardButton(text=f"{num}")
        kb.add(button)
    return kb

def del_mes(msg: types.Message):
    msg.delete()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)