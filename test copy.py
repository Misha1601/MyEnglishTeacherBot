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



if __name__ == "__main__":
    select_word(['cat', 'dog', 'elephant'])
