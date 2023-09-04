from aiogram import types
import os
import random
import json
from main import bot
from bot.keyboards import buttons_answer, buttons_no_menu
from main import db

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

# 1. Создаем 3 словаря
# - словарь всех слов (копируем из json файла). Те слова, что ушли для изучения удаляются из словаря. Если словарь оказался пустой, или в неём оказалось меньше
# 5 слов, в словарь для изучения копируем оставшиеся слова, загружаем слова из нового словаря (или повторно), и рандомно докопируем оставшиеся слова.
# - слоаврь изучаемых в данный момент слов. учим по 5 (или 10) слов. Слова считаются выученными,
# когда нет ни одной ошибки при 5 циклах повторения. Слова по кнопке "потренеруемся ещё" берутся из словаря выученных слов
# - словарь выученных слов. В данный словарь попадают все слова, которые 5 циклов подряд не дали ни одной ошибки. Каждое слово несет информацию о количестве допущенных в нем ошибок.
# Данные слова идут только по кнопке "потренеруемся еще!". Слова даются те, на которые было допущено больше всего ошибок.

def escape_markdownv2(text):
    reserved_chars = '\\_*[]()~`>#+-=|{}.!'
    escaped_text = ''
    for char in text:
        if char in reserved_chars:
            escaped_text += '\\' + char
        else:
            escaped_text += char
    return escaped_text

def generate_offer(mes_or_key):
    word = random.choice(list(data1.keys()))
    word_translate = data1[word]
    return (word, word_translate)

# вывести в отдельную функцию генерацию ответа offer_and_translate
def offer_and_translate(mes_or_key):
    word = generate_offer(mes_or_key)
    word2 = escape_markdownv2(word[1][1])
    offer = f"{word[0]}\n ||{word[1][0]}, {word2}||"
    return offer

async def game(message_or_key):
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
    # добавляем в БД запись об отправке сообщения, и помечаем его для дальнейшего удаления
    db.add_message(id_chat=mes1.chat['id'], id_message=mes1['message_id'], delete=1)
    # добавляем запись со словом
    db.add_message(id_chat=mes.chat['id'], id_message=mes['message_id'], word=word)


if __name__ == "__main__":
    print(offer_and_translate('123'))
