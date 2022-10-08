import random
from parts_of_speech.pronoun import PeP


class Offer_g():
    """получаем какое либо слово и генерируем на его основе предложение"""

    def __init__(self, word):
        self.word = word

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


    def generator(self):
        pronoun = random.choice(tuple(PeP.keys()))
        fg = f"Will {pronoun} {self.word}?"
        fs = f"{pronoun} will {self.word}".capitalize()
        fn = f"{pronoun} will not {self.word}".capitalize()
        prq = f"{self.do_or_does_question(pronoun)} {self.word}?"
        prs = f"{pronoun} {self.word}".capitalize() if pronoun not in ('he', 'she') else f"{pronoun} {self.word}s".capitalize()
        prn = f"{self.do_or_does_negation(pronoun)} {self.word}"
        paq = f"Did {pronoun} {self.word}?"
        pas = f"{pronoun} did not {self.word}d".capitalize()
        pan = f"{pronoun} did not {self.word}".capitalize()
        return random.choice([fg, fs, fn, prq, prs, prn, paq, pas, pan])


if __name__ == "__main__":
    word = Offer_g("love")
    print(word.generator())
    # print(list(PeP.keys()))
