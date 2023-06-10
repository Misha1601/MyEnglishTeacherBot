import json
from app import db
import os

def merge_json_files():
    json_files = ['/home/misha/Python/MyEnglishTeacherBot/app/word_collection1/word_3-5.json']

    # Создаем пустой словарь для объединения данных из JSON файлов
    merged_data = {}

    # Цикл по списку JSON файлов
    for file_name in json_files:
        # Открываем текущий файл на чтение
        with open(file_name, 'r') as file:
            # Считываем данные из файла и парсим их в словарь
            data = json.load(file)



# Вызываем функцию для объединения JSON файлов в текущей директории
merge_json_files()