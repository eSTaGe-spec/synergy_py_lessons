"""
Задание №1

Сначала вводится число N, затем вводится ровно N целых чисел.
Подсчитайте, сколько из них равны нулю, и выведите это количество
"""

number = int(input('Введите число: '))

count_0 = 0
for num in range(1, number+1):
    new_num = int(input(f'Введите число №{num}: '))
    if new_num == 0:
        count_0 += 1

print(f'Кол-во чисел равных нулю: {count_0}')
