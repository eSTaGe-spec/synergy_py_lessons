"""
Задание №3

Вводятся целые числа A и B. Гарантируется, что A ≤ B. Выведите все четные числа на заданном отрезке через пробел.

"""

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

if num1 <= num2:
    for number in range(num1, num2+1):
        if number % 2 == 0:
            print(number, end=' ')
else:
    print('Первое число должно быть меньше или равно второму')