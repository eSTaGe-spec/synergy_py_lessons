"""
Задание №1

Пользователь вводит целое число. Выведите его строку-описание вида "отрицательное четное число", "нулевое число",
"положительное нечетное число", например, численным описанием числа 190 является строка "положительное четное число".
Если число не является четным - выведите сообщение "число не является четным"
"""

number = int(input('Введите целое число: '))

if number != 0:
    if number % 2 == 0:
        if number > 0:
            print('Положительное четное число')
        else:
            print('Отрицательное четное число')
    else:
        print('Число не является четным')

else:
    print('Нулевое число')
