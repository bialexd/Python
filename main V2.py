import json
import random


attempts = 0
d = []
games = 0


def main():
    is_new_player(name)
    main_menu()


def get_name():
    try:
        name = input("Введите своё имя: ")
    except KeyboardInterrupt:
        exit()
    return name


name = get_name()


def magic():
    def game():
        global attempts
        global games
        diapason()
        number = generation_number()
        gam = 0
        att = 0
        games += 1
        gam += 1
        while True:
            g = guess()
            if g is not False:
                if number != g:
                    att += 1
                    attempts += 1
                    if number > g:
                        print("Вы не угадали. Ваше число меньше чем загаданое!")
                    else:
                        print("Вы не угадали. Ваше число больше чем загаданое!")
                else:
                    break
        att += 1
        attempts += 1
        print("Вы угадали!" + " Число попыток: " + str(att))
        is_record(att)
        try:
            restart = input("Вы хотите перезапустить программу(Y/N)")
        except KeyboardInterrupt:
            exit()
        if restart.lower() == "y" or restart == "":
            data = json.load(open('data.json'))
            data[name]['attempts'] += att
            data[name]['games'] += gam
            with open('data.json', 'w') as f:
                data = json.dumps(data, indent=4)
                f.write(data)
            game()
        else:
            data = json.load(open('data.json'))
            data[name]['attempts'] += att
            data[name]['games'] += gam
            avg_attempts = data[name]['attempts'] / data[name]['games']
            data[name]['avg_attempts'] = round(avg_attempts, 2)
            with open('data.json', 'w') as f:
                data = json.dumps(data, indent=4)
                f.write(data)
            main_menu()

    def is_record(a):
        with open('data.json') as f:
            data = json.load(f)
            if data[name]['record'] is None or data[name]['record'] > a:
                print("Новый рекорд!")
                data[name]['record'] = a
                with open('data.json', 'w') as f:
                    data = json.dumps(data, indent=4)
                    f.write(data)
            else:
                pass

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
        global d
        d.clear()
        try:
            min_ = input("Введите минимальное число диапазона: ")
            max_ = input("Введите максимальное число диапазона: ")
        except KeyboardInterrupt:
            exit()
        if is_value_true(min_, max_):
            d.append(int(min_))
            d.append(int(max_))
            return True
        else:
            print("Вы ввели не числа!/Минимальное число диапазона больше чем максимальное число диапазона!")
            diapason()

    def generation_number():
        print(d)
        number = random.randint(d[0], d[1])
        return number

    def is_value_of_number(number):
        try:
            int(number)
            return True
        except ValueError:
            return False

    def guess():
        try:
            guess_number = input("Какое число загадано: ")
        except KeyboardInterrupt:
            exit()
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
    try:
        what = input("Введите номер пункта который Вы хотите выбрать: ")
    except KeyboardInterrupt:
        exit()
    if what == "1":
        magic()
    elif what == "2":
        show_stat()
        main_menu()
    elif what == "3":
        print("Привет! Меня зовут Саша, я сделал эту недопрограмму")
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


def show_stat():
    with open('data.json') as f:
        data = json.load(f)
        for i in data:
            if str(i) == str(name):
                print("Имя: " + str(i) + "(Вы)")
            else:
                print("Имя: " + str(i))
            if data[i]['record'] is None:
                print("Рекордное количество попыток: Нет")
            else:
                print("Рекордное количество попыток: " + str(data[i]['record']))
            print("Количество попыток: " + str(data[i]['attempts']))
            print("Количество игр: " + str(data[i]['games']))
            if data[i]['avg_attempts'] is None:
                print("Среднее количество попыток: Нет")
            else:
                print("Среднее количество попыток: " + str(data[i]['avg_attempts']))
            print("")


if __name__ == '__main__':
    main()
