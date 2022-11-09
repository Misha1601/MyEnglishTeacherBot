from translatepy import Translator

class Translate:
    """Класс для перевода слова, предложения ...
       Необходимо передать 1 обязательный параметр str"""

    def __init__(self, word:str):
        self.word = word

    def perevod(self):
        translator = Translator()
        result = translator.translate(self.word, "ru")
        return result


if __name__ == "__main__":
    a = Translate('Hello world').perevod()
    print(a)