import builtins
import json
from translatepy import Translator
from translatepy.translators.google import GoogleTranslate
from translatepy.translators.yandex import YandexTranslate
from translatepy.translators.deepl import DeeplTranslate

class Translate:
    """Класс для перевода слова, предложения ...
       Необходимо передать 1 обязательный параметр str"""

    def __init__(self, word:str):
        self.word = word

    def perevod(self):
        # translator = Translator()
        translator_g = GoogleTranslate()
        translator_y = YandexTranslate()
        translator_d = DeeplTranslate()
        # result = translator.translate(self.word, "ru")
        try:
            result_g = translator_g.translate(self.word, "ru")
        except Exception:
            result_g = "Гугл не смог перевести\!"
        try:
            result_y = translator_y.translate(self.word, "ru")
        except Exception:
            result_y = "Яндекс не смог перевести\!"
        try:
            result_d = translator_d.translate(self.word, "ru")
        except Exception:
            result_d = "DeepL не смог перевести\!"
        return (str(result_g), str(result_y), str(result_d))

def get_py_builtins():
    py_builtins = {}
    for name in dir(builtins):
        obj = getattr(builtins, name)

        # Исключаем методы и атрибуты, начинающиеся с "dunders"
        # и методы, заканчивающиеся на "_"
        if name.startswith("__") or name.endswith("_"):
            continue

        # Для каждого типа данных Python создаем словарь
        # с его описанием и списком его методов с описаниями
        if isinstance(obj, type):
            doc = obj.__doc__
            methods = {}
            for method_name in dir(obj):
                if method_name.startswith("__") or method_name.endswith("_"):
                    continue
                method_obj = getattr(obj, method_name)
                if not method_obj.__doc__:
                    methods[method_name] = {"en": method_obj.__doc__, "ru":'Нету описания'}
                else:
                    perevod_method_name = Translate(method_obj.__doc__).perevod()
                    methods[method_name] = {"en": method_obj.__doc__, "ru":perevod_method_name[0]}
            perevod_methods = Translate(doc).perevod()
            py_builtins[name] = {"description": {"en":doc, "ru":perevod_methods[0]}, "methods": methods}

    # Возвращаем JSON с встроенными типами данных Python, их описанием и методами с описаниями
    return py_builtins

# print(get_py_builtins())
# print(len(get_py_builtins()))
# print(get_py_builtins()['list'])

# with open('py111.json', 'w', encoding='utf-8') as outfile:
#         # Записываем объединенные данные в виде JSON
#         json.dump(get_py_builtins(), outfile, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    # a = Translate('Hello world').perevod()
    # print(type(a[0]))
    # print(a[1])
    # print(a[2])
    with open('perevod.json', 'w', encoding='utf-8') as outfile:
        # Записываем объединенные данные в виде JSON
        json.dump(get_py_builtins(), outfile, ensure_ascii=False, indent=4)