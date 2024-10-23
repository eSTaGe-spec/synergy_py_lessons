"""
Задание №2

Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв?
Гласными называют буквы «a», «e», «i», «o», «u».

Для решения задачи создайте переменную и в неё положите слово с помощью input()

А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False
"""

word = input('Введите слово из латинских букв: ')
let_a = 0
let_e = 0
let_i = 0
let_o = 0
let_u = 0

if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word:
    for letter in word:
        if letter == 'a':
            let_a += 1
        elif letter == 'e':
            let_e += 1
        elif letter == 'i':
            let_i += 1
        elif letter == 'o':
            let_o += 1
        elif letter == 'u':
            let_u += 1

    print(f'Кол-во буквы "a": {let_a}\n'
          f'Кол-во буквы "e": {let_e}\n'
          f'Кол-во буквы "i": {let_i}\n'
          f'Кол-во буквы "o": {let_o}\n'
          f'Кол-во буквы "u": {let_u}')

else:
    print(False)


