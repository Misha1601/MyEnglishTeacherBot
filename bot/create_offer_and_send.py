from aiogram import types
import os
import random
import json
from main import bot
from bot.keyboards import buttons_answer, buttons_no_menu
from bot.data import del_old_messege, save_info_messege, statistics

file_list = os.getcwd()

if os.name == 'posix':
    json_files = [file_list+'/app/word_collection1/word_3-5.json'
#                   file_list+'/app/word_collection1/word_gl_fras.json',
#                   file_list+'/app/word_collection1/word_gl_modl.json',
#                   file_list+'/app/word_collection1/word_gl_nepr.json',
#                   file_list+'/app/word_collection1/word_gl_pr.json'
                  ]
else:
    json_files = [file_list+'\\app\word_collection1\word_3-5.json'
#                   file_list+'\\app\word_collection1\word_gl_fras.json',
#                   file_list+'\\app\word_collection1\word_gl_modl.json',
#                   file_list+'\\app\word_collection1\word_gl_nepr.json',
#                   file_list+'\\app\word_collection1\word_gl_pr.json'
                    ]
with open(json_files[0], 'r', encoding='utf-8') as file:
    data1 = json.load(file)

def generate_offer(mes_or_key):
    import bot.data as data
    word = random.choice(list(data1.keys()))
    word_translate = data1[word]
    if str(mes_or_key).isnumeric():
        data.WORD[mes_or_key] = [word, word_translate]
    else:
        data.WORD[mes_or_key.chat.id] = [word, word_translate]
    return (word, word_translate)

# вывести в отдельную функцию генерацию ответа offer_and_translate
def offer_and_translate(mes_or_key):
    word = generate_offer(mes_or_key)
    offer = f"{word[0]}\n ||{word[1]}||"
    return offer


async def game(message_or_key): # сделать принимающим 1 параметр, его проверка реализована в генерации
    word = offer_and_translate(message_or_key)

    if str(message_or_key).isnumeric():
        mes = await bot.send_message(message_or_key, f"{word}",
                                    parse_mode='MarkdownV2',
                                    reply_markup=buttons_answer())
        mes1 = await bot.send_message(message_or_key, f"В любом обучении главное практика на постоянной основе!",
                                       reply_markup=buttons_no_menu())
    else:
        mes = await message_or_key.answer(f"{word}",
                                    parse_mode='MarkdownV2',
                                    reply_markup=buttons_answer())
        mes1 = await message_or_key.answer(f"В любом обучении главное практика на постоянной основе!",
                                       reply_markup=buttons_no_menu())
    await del_old_messege(mes)
    await save_info_messege(mes)
    await save_info_messege(mes1)
    await statistics(message=mes, quest=True)

if __name__ == "__main__":
    print(offer_and_translate('123'))
