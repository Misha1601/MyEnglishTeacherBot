from aiogram import types
import os
import random
import json
# from main import bot
# from bot.keyboards import buttons_answer, buttons_no_menu
# from main import db

file_list = os.getcwd()

if os.name == 'posix':
    json_files = [file_list+'/app/word_3-5.json']
    json_files2 = [file_list+'/app/perevod_no_error.json']
else:
    json_files = [file_list+'\\app\word_3-5.json']
    json_files2 = [file_list+'\\app\perevod_no_error.json']


with open(json_files[0], 'r', encoding='utf-8') as file:
    data1 = json.load(file)

with open(json_files2[0], 'r', encoding='utf-8') as file:
    word_metod = json.load(file)

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
    word = random.choice(list(word_metod.keys()))
    word_translate_en = word_metod[word]["description"]["en"]
    word_translate_ru = word_metod[word]["description"]["ru"]
    metod_word = random.choice(list(word_metod[word]["methods"].keys()))
    metod_word_en = word_metod[word]["methods"][metod_word]["en"]
    metod_word_ru = word_metod[word]["methods"][metod_word]["ru"]
    return (word, word_translate_en, word_translate_ru, metod_word, metod_word_en, metod_word_ru)

# вывести в отдельную функцию генерацию ответа offer_and_translate
def offer_and_translate(mes_or_key):
    word = generate_offer(mes_or_key)

    word0 = word[0]
    word1 = escape_markdownv2(word[1])
    word2 = escape_markdownv2(word[2])
    word3 = word[3]
    word4 = escape_markdownv2(word[4])
    word5 = escape_markdownv2(word[5])

    offer = f"Что за тип {word0}, что выполняет его метод {word3}\n ||{word1}\n{word2} \n\n{word4}\n{word5}||"

    return offer

async def play_game(message_or_key):
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
    # met = generate_offer('123')
    # print(met[0])
    # print(met[1])
    # print(met[2])
    # print(met[3])
    # print(met[4])
    # print(met[5])
