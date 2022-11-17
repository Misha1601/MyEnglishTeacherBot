from aiogram import types
from main import bot
from bot.keyboards import buttons_answer, buttons_no_menu
from app.generator import Generate
from app.translate import Translate
from app.data import del_old_messege, save_info_messege, statistics


async def generate_offer(message: types.Message):
    import app.data as data
    word = Generate().offer()
    word_translate = Translate(word=word).perevod()
    data.WORD[message.chat.id] = [word, word_translate]
    return (word, word_translate)

async def game(message: types.Message = None, key = None):
    word = await generate_offer(message)
    if key:
        mes = await bot.send_message(key, f"{word[0]}\n"
                                    f"||Google \- {word[1][1]}\n||"
                                    f"||Yandex \- {word[1][2]}\n||"
                                    f"||Deepl \- {word[1][3]}\n||",
                                    parse_mode='MarkdownV2',
                                    reply_markup=buttons_answer())
        mes1 = await bot.send_message(key, f"В любом обучении главное практика на постоянной основе!",
                                       reply_markup=buttons_no_menu())
    else:
        mes = await message.answer(f"{word[0]}\n"
                                    f"||Google \- {word[1][1]}||\n"
                                    f"||Yandex \- {word[1][2]}||\n"
                                    f"||Deepl \- {word[1][3]}||\n",
                                    parse_mode='MarkdownV2',
                                    reply_markup=buttons_answer())
        mes1 = await message.answer(f"В любом обучении главное практика на постоянной основе!",
                                       reply_markup=buttons_no_menu())
        await message.delete()
    await del_old_messege(mes)
    await save_info_messege(mes)
    await save_info_messege(mes1)
    await statistics(message=mes, quest=True)
