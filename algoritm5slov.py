def select_word(list_word):
    yes_list = list_word.copy()
    no_list = []
    n = 3 # количество безошибочного повтора слов
    k = 0 # счетчик повторений
    while k < n:
        index = 0
        k += 1
        while index < len(yes_list):
            answer = input(f"Вы запомнили это слово {yes_list[index]}? Ответьте 'да' или 'нет': ").lower()
            if answer == 'нет':
                if n > 0:
                    k = 0
                no_list.append(yes_list.pop(index))
            elif answer == 'да':
                index += 1
            else:
                print('Вы не то ввели, давайте повторим ещё раз!')
        print(yes_list)
        print(no_list)

        while no_list:
            print(no_list)
            answer = input(f"Вы запомнили это слово {no_list[0]} (из списка no_list)? Ответьте 'да' или 'нет': ").lower()
            if answer == 'да':
                yes_list.append(no_list.pop(0))
            elif answer == 'нет':
                no_list.append(no_list.pop(0))
            else:
                print('Вы не то ввели, давайте повторим ещё раз!')

def game():
    # Назначаем переменной m по сколько слов будем забирать из словаря для изучения
    # и n количество безошибочного повторения группы слов, k счетчик повторений
    # 1. Проверяем слоаврь со словами
    # 2. Если словарь пустой, загружаем его повторно, если нет, продолжаем
    # 3. Проверяем сколько осталось слов в словаре, если меньше n сохраняем все в новый словарь удаляя из
    # основного через pop, иначе идём далее
    # 4. Случайным образом выбираем n слов, сохраняем его в новый словарь удаляя из основного через pop
    # 5. Создаем два спаска yes_list с ключами нового словаря и no_list пустой
    # 6. далее алгоритм функции select_word
    ...


if __name__ == "__main__":
    select_word(['cat', 'dog', 'elephant'])
