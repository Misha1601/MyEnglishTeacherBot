import json
import os

def merge_json_files():
    json_files = ['/home/misha/Python/MyEnglishTeacherBot/app/word_collection1/word_3.json',
                  '/home/misha/Python/MyEnglishTeacherBot/app/word_collection1/word_4.json',
                  '/home/misha/Python/MyEnglishTeacherBot/app/word_collection1/word_5.json']

    # Создаем пустой словарь для объединения данных из JSON файлов
    merged_data = {}

    # Цикл по списку JSON файлов
    for file_name in json_files:
        # Открываем текущий файл на чтение
        with open(file_name, 'r') as file:
            # Считываем данные из файла и парсим их в словарь
            data = json.load(file)
            # Объединяем данные из файла со всеми предыдущими данными
            merged_data.update(data)

    # Открываем новый файл на запись
    with open('word3-5.json', 'w', encoding='utf-8') as outfile:
        # Записываем объединенные данные в виде JSON
        json.dump(merged_data, outfile, ensure_ascii=False, indent=4)

# Вызываем функцию для объединения JSON файлов в текущей директории
merge_json_files()