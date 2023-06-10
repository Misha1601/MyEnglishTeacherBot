import random

# создаем тестовый словарь из списка слов
dictionary = ['apple', 'banana', 'cat', 'dog', 'elephant']

# создаем словарь ответов
answers = {}

def select_word():
    # сортируем словарь ответов по возрастанию интервала повторения
    sorted_answers = sorted(answers.items(), key=lambda x: x[1])

    # выбираем случайное слово из словаря
    word = random.choice(dictionary)

    # если в ответах уже есть это слово, выбираем его повторно и увеличиваем интервал повторения
    if word in answers:
        answers[word] += 1
    # если в ответах нет этого слова, выбираем его и устанавливаем интервал повторения в 1
    else:
        answers[word] = 1

    # если интервал повторения у слова меньше 1, устанавливаем его равным 1
    if answers[word] < 1:
        answers[word] = 1

    # устанавливаем вероятность повторения слова (на основе интервала повторения)
    probability = 1 / answers[word]

    # если загаданное слово должно быть повторено в следующем запросе, выбираем его
    if random.random() < probability:
        return word
    # если слово не должно быть повторено, выбираем слово с самым коротким интервалом повторения
    else:
        # выбираем первое слово из отсортированного списка
        return sorted_answers[0][0]

if __name__ == "__main__":
    for i in [i for i in range(100)]:
        print(select_word())
    print(answers)