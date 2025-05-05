print("При обнаружении багов пишите мне на почту - pythonerkk@mail.ru")
print("Нужно кинуть скрин недоработки")
print()
print("______________________________________________________")
print()

from random import randint
balans = 0
# Вход + добавить цикл ко всей игре и условие выхода из игры
def Game():
    global balans
    print('Выбери уровень сложности:')
    print('1 уровень от 1 до 100')
    print('2 уровень от 1 до 250')
    print('3 уровень от 1 до 500')
    print("4 уровень от 1 до 1000")
    print("5 уровень от 1 до 2000")
    g = False
    while g != True:
        try:
            y = int(input("Введи номер уровня: "))
            if y == 1 or y == 2 or y ==3 or y == 4 or y == 5:
                g =True
            else:
                print("Введите целое число от 1 до 5")
        except ValueError:
            print('Ошибка! Введите целое число от 1 до 5')


    # 1 уровень
    if y == 1:
        x = randint(1, 100)
        g = False
        print('Угадай число от 1 до 100 за 6 попыток. За лишнию попытку у тебя будет сниматься по 100 очков')
        print("За прохождение 1 уровня можно получить 500 очков")
        i = 0
        while g != True:
            i += 1
            try:
                a = int(input(f'Твоя {i} попытка - '))
                g =True
            except ValueError:
                print('Ошибка! Введите целое число')
        h = True
        while a!=x:
            if h == True:
                if a > x:
                    print('Много. Попробуй ввести число меньшего значения')
                elif a < x:
                    print('Мало. Попробуй ввести число большего значения')
            i += 1
            try:
                a = int(input(f'Твоя {i} попытка - '))
                h = True
            except ValueError:
                print('Ошибка! Введите целое число')
                h = False
        if a == x:
            if i <= 6:
                count = 500
            else:
                count = 500 - ((i - 6) * 100)
                if count < 0:
                    count = 0
            balans += count
            print()
            print("______________________________________________________")
            print()
            print('Молодец! Ты угадал число. Твой счёт увеличился на',count, "очков")


    # 2 уровень
    if y == 2:
        x = randint(1, 250)
        g = False
        print('Угадай число от 1 до 250 за 7 попыток. За лишнию попытку у тебя будет сниматься по 100 очков')
        print("За прохождение 2 уровня можно получить 800 очков")
        i = 0
        while g != True:
            i += 1
            try:
                a = int(input(f'Твоя {i} попытка - '))
                g =True
            except ValueError:
                print('Ошибка! Введите целое число')
        h = True
        while a!=x:
            if h == True:
                if a > x:
                    print('Много. Попробуй ввести число меньшего значения')
                elif a < x:
                    print('Мало. Попробуй ввести число большего значения')
            i += 1
            try:
                a = int(input(f'Твоя {i} попытка - '))
                h = True
            except ValueError:
                print('Ошибка! Введите целое число')
                h = False
        if a == x:
            if i <= 7:
                count = 800
            else:
                count = 800 - ((i - 7) * 100)
                if count < 0:
                    count = 0
            balans += count
            print()
            print("______________________________________________________")
            print()
            print('Молодец! Ты угадал число. Твой счёт увеличился на',count, "очков")

    # 3 уровень
    if y == 3:
        x = randint(1, 500)
        g = False
        print('Угадай число от 1 до 500 за 8 попыток. За лишнию попытку у тебя будет сниматься по 100 очков')
        print("За прохождение 3 уровня можно получить 1000 очков")
        i = 0
        while g != True:
            i += 1
            try:
                a = int(input(f'Твоя {i} попытка - '))
                g = True
            except ValueError:
                print('Ошибка! Введите целое число')
        h = True
        while a != x:
            if h == True:
                if a > x:
                    print('Много. Попробуй ввести число меньшего значения')
                elif a < x:
                    print('Мало. Попробуй ввести число большего значения')
            i += 1
            try:
                a = int(input(f'Твоя {i} попытка - '))
                h = True
            except ValueError:
                print('Ошибка! Введите целое число')
                h = False
        if a == x:
            if i <= 8:
                count = 1000
            else:
                count = 1000 - ((i - 8) * 100)
                if count < 0:
                    count = 0
            balans += count
            print()
            print("______________________________________________________")
            print()
            print('Молодец! Ты угадал число. Твой счёт увеличился на',count, "очков")


    #4 уровень
    if y == 4:
        x = randint(1, 1000)
        g = False
        print('Угадай число от 1 до 1000 за 9 попыток. За лишнию попытку у тебя будет сниматься по 100 очков')
        print("За прохождение 4 уровня можно получить 1200 очков")
        i = 0
        while g != True:
            i += 1
            try:
                a = int(input(f'Твоя {i} попытка - '))
                g =True
            except ValueError:
                print('Ошибка! Введите целое число')
        h = True
        while a!=x:
            if h == True:
                if a > x:
                    print('Много. Попробуй ввести число меньшего значения')
                elif a < x:
                    print('Мало. Попробуй ввести число большего значения')
            i += 1
            try:
                a = int(input(f'Твоя {i} попытка - '))
                h = True
            except ValueError:
                print('Ошибка! Введите целое число')
                h = False
        if a == x:
            if i <= 9:
                count = 1200
            else:
                count = 1200 - ((i - 9) * 100)
                if count < 0:
                    count = 0
            balans += count
            print('Молодец! Ты угадал число. Твой счёт увеличился на',count, "очков")

    #5 уровень
    if y == 5:
        x = randint(1, 2000)
        g = False
        print('Угадай число от 1 до 2000 за 10 попыток. За лишнию попытку у тебя будет сниматься по 100 очков')
        print("За прохождение 5 уровня можно получить 1500 очков")
        i = 0
        while g != True:
            i += 1
            try:
                a = int(input(f'Твоя {i} попытка - '))
                g =True
            except ValueError:
                print('Ошибка! Введите целое число')
        h = True
        while a!=x:
            if h == True:
                if a > x:
                    print('Много. Попробуй ввести число меньшего значения')
                elif a < x:
                    print('Мало. Попробуй ввести число большего значения')
            i += 1
            try:
                a = int(input(f'Твоя {i} попытка - '))
                h = True
            except ValueError:
                print('Ошибка! Введите целое число')
                h = False
        if a == x:
            if i <= 10:
                count = 1500
            else:
                count = 1500 - ((i - 10) * 100)
                if count < 0:
                    count = 0
            balans += count
            print('Молодец! Ты угадал число. Твой счёт увеличился на',count, "очков")

print("Твой общий счёт =", balans)
print()
print("______________________________________________________")
print()
Game()
close = ""
while close.lower() != "нет":
    print()
    print("______________________________________________________")
    print()
    print("Твой общий счёт =", balans)
    print("Продолжаем игру?")
    close = input()
    print()
    print("______________________________________________________")
    print()
    if close.lower() == "да":
        Game()
    elif close.lower() == "нет":
        continue
    else:
        print("Напиши да или нет")
print("Для закрытия консоли нажми 'ENTER'")
print("Made by MicheZZ")
input()




