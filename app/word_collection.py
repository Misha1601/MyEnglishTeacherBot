# Словарь местоимений (pronoun)
pronoun = {"PeP":{"I":["я"],
                  "you":["ты", "вы"],
                  "we":["мы"],
                  "they":["они"],
                  "he":["он"],
                  "she":["она"]},
           "PoP":{"my":["мой"],
                  "your":["твой, ваши"],
                  "our":["наш"],
                  "their":["их"],
                  "hes":["его"],
                  "her":["её"]}
           }
# Словарь прилагательных (adjective)
adjective = {}
# Словарь наречий (adverb)
adverb = {}
# Словарь числительных (numerals)
numerals = {}
# Словарь существительных (noun)
noun = {}
# Словарь глаголов (verb)
verb = {"correct":{"love" : ["любить"], "play" : ["играть"]},
        "incorrect":{}
        }
if __name__ == "__main__":
    print(list(verb.get('correct').keys()))
    print(list(verb.keys()))