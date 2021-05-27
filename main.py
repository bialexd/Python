import json
import math
import random

d = []
record = None
attempts = 0


def main():
    is_new_player(name)
    main_menu()


def get_name():
    name = input("Введите своё имя: ")
    return name


name = get_name()


def magic():
    def game():
        global attempts
        global record
        games = 0
        diapason()
        number = generation_number()
        while True:
            g = guess()
            if g is not False:
                if number != g:
                    attempts += 1
                    if number > g:
                        print("Вы не угадали. Ваше число меньше чем загаданое!")
                    else:
                        print("Вы не угадали. Ваше число больше чем загаданое!")
                else:
                    break
        print("Вы угадали!" + " Число попыток: " + str(attempts))
        is_record(attempts)
        restart = input("Вы хотите перезапустить программу(Y/N)")
        if restart.lower() == "y" or restart == "":
            games += 1
            game()
        else:
            games += 1
            data = json.load(open('data.json'))
            data[name]['attempts'] += attempts
            data[name]['games'] += games
            avg_attempts = attempts / games
            data[name]['avg_attempts'] = math.ceil(avg_attempts)
            if data[name]['record'] is None or data[name]['record'] > record:
                data[name]['record'] = record
            else:
                pass
            with open('data.json', 'w') as f:
                data = json.dumps(data, indent=4)
                f.write(data)
            main_menu()

    def is_record(a):
        global record
        with open('data.json') as f:
            data = json.load(f)
            if data[name]['record'] is None or data[name]['record'] > a:
                print("Новый рекорд!")
                record = a

    def is_value_true(min_, max_):
        try:
            int(min_)
            int(max_)
            if int(max_) > int(min_):
                return True
            else:
                return False
        except ValueError:
            return False

    def diapason():
        min_ = input("Введите минимальное число диапазона: ")
        max_ = input("Введите максимальное число диапазона: ")
        if is_value_true(min_, max_):
            d.append(int(min_))
            d.append(int(max_))
            return True
        else:
            print("Вы ввели не числа!/Минимальное число диапазона больше чем максимальное число диапазона!")
            diapason()

    def generation_number():
        global d
        number = random.randint(d[0], d[1])
        return number

    def is_value_of_number(number):
        try:
            int(number)
            return True
        except ValueError:
            return False

    def guess():
        guess_number = input("Какое число загадано: ")
        if is_value_of_number(guess_number):
            return int(guess_number)
        else:
            print("Вы ввели не число!")
            return False

    if __name__ == '__main__':
        print("Правила игры: нужно угадать число! ")
        game()


def main_menu():
    global name
    print("1. Magic")
    print("2. Посмотреть статистику")
    print("3. О создателе")
    print("4. Выход")
    what = input("Введите номер пункта который Вы хотите выбрать: ")
    if what == "1":
        magic()
    elif what == "2":
        show_stat(name)
        main_menu()
    elif what == "3":
        print("Привет! Меня зовут Саша, я зделал эту недо программу")
        main_menu()
    elif what == "4":
        exit()
    else:
        print("Вы выбрали не сущевствующий вариант!")
        main_menu()


def is_new_player(name):
    try:
        with open('data.json') as f:
            try:
                data = json.load(f)
                if name in data:
                    pass
                else:
                    data[name] = {'record': None, 'attempts': 0, 'games': 0, 'avg_attempts': None}
                    with open('data.json', 'w') as f:
                        data = json.dumps(data, indent=4)
                        f.write(data)
            except Exception:
                a = {name: {'record': None, 'attempts': 0, 'games': 0, 'avg_attempts': None}}
                with open('data.json', 'w') as f:
                    a = json.dumps(a, indent=4)
                    f.write(a)
    except FileNotFoundError:
        a = {name: {'record': None, 'attempts': 0, 'games': 0, 'avg_attempts': None}}
        with open('data.json', 'w') as f:
            a = json.dumps(a, indent=4)
            f.write(a)


def show_stat(name):
    with open('data.json') as f:
        data = json.load(f)
        print("Имя: " + str(name))
        if data[name]['record'] is None:
            print("Рекордное количество попыток: Нет")
        else:
            print("Рекордное количество попыток: " + str(data[name]['record']))
        print("Количество попыток: " + str(data[name]['attempts']))
        print("Количество игр: " + str(data[name]['games']))
        if data[name]['avg_attempts'] is None:
            print("Среднее количество попыток: Нет")
        else:
            print("Среднее количество попыток: " + str(data[name]['avg_attempts']))


if __name__ == '__main__':
    main()
