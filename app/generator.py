import random
from . import word_collection
# import word_collection


class Generate:
    """Класс для генерации предложения, слова или ...
       для генерации необходимо вызвать соответствующий метод
       (на данном этапе генерируем только предложение, метод Generate().offer())"""

    def do_or_does_question(self, pronoun):
        p = ("he", "she")
        if pronoun in p:
            return f"Does {pronoun}"
        else:
            return f"Do {pronoun}"

    def do_or_does_negation(self, pronoun):
        p = ("he", "she")
        if pronoun in p:
            return f"{pronoun} doesn’t".capitalize()
        else:
            return f"{pronoun} don’t".capitalize()


    def offer(self):
        word = random.choice(tuple(word_collection.verb.get('correct').keys()))
        pronoun = random.choice(tuple(word_collection.pronoun.get('PeP').keys()))
        fg = f"Will {pronoun} {word}?"
        fs = f"{pronoun} will {word}".capitalize()
        fn = f"{pronoun} will not {word}".capitalize()
        prq = f"{self.do_or_does_question(pronoun)} {word}?"
        prs = f"{pronoun} {word}".capitalize() if pronoun not in ('he', 'she') else f"{pronoun} {word}s".capitalize()
        prn = f"{self.do_or_does_negation(pronoun)} {word}"
        paq = f"Did {pronoun} {word}?"
        pas = f"{pronoun} did not {word}d".capitalize()
        pan = f"{pronoun} did not {word}".capitalize()
        return random.choice([fg, fs, fn, prq, prs, prn, paq, pas, pan])


if __name__ == "__main__":
    print(Generate().offer())
