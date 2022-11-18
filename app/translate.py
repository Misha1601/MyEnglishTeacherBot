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
        translator = Translator()
        translator_g = GoogleTranslate()
        translator_y = YandexTranslate()
        translator_d = DeeplTranslate()
        # result = translator.translate(self.word, "ru")
        try:
            result_g = translator_g.translate(self.word, "ru")
        except Exception:
            result_g = "Гугл не смог перевести!"
        try:
            result_y = translator_y.translate(self.word, "ru")
        except Exception:
            result_y = "Яндекс не смог перевести!"
        try:
            result_d = translator_d.translate(self.word, "ru")
        except Exception:
            result_d = "DeepL не смог перевести!"
        return (result_g, result_y, result_d)


if __name__ == "__main__":
    a = Translate('Hello world').perevod()
    print(a[0])
    print(a[1])
    print(a[2])