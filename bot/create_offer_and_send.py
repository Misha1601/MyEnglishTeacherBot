from aiogram import types
from main import bot
from bot.keyboards import buttons_answer, buttons_no_menu
from app.generator import Generate
from app.translate import Translate
from app.data import del_old_messege, save_info_messege, statistics


def generate_offer(mes_or_key):
    import app.data as data
    word = Generate().offer()
    word_translate = Translate(word=word).perevod()
    if str(mes_or_key).isnumeric():
        data.WORD[mes_or_key] = [word, word_translate]
    else:
        data.WORD[mes_or_key.chat.id] = [word, word_translate]
    return (word, word_translate)

# вывести в отдельную функцию генерацию ответа offer_and_translate
def offer_and_translate(mes_or_key):
    word = generate_offer(mes_or_key)
    offer = f"{word[0]}\n ||Google \- {word[1][0]}||\n||Yandex \- {word[1][1]}||\n||Deepl \- {word[1][2]}||"
    # offer = "hello world"
    return offer


async def game(message_or_key): # сделать принимающим 1 параметр, его проверка реализована в генерации
    word = offer_and_translate(message_or_key)

    if str(message_or_key).isnumeric():
        mes = await bot.send_message(message_or_key, f"{word}",
                                    parse_mode='MarkdownV2',
                                    reply_markup=buttons_answer())
        mes1 = await bot.send_message(message_or_key, f"В любом обучении главное практика на постоянной основе\!",
                                       reply_markup=buttons_no_menu())
    else:
        mes = await message_or_key.answer(f"{word}",
                                    parse_mode='MarkdownV2',
                                    reply_markup=buttons_answer())
        mes1 = await message_or_key.answer(f"В любом обучении главное практика на постоянной основе\!",
                                       reply_markup=buttons_no_menu())
        await message_or_key.delete()
    await del_old_messege(mes)
    await save_info_messege(mes)
    await save_info_messege(mes1)
    await statistics(message=mes, quest=True)
