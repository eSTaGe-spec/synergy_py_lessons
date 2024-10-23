"""
Задание №3

Два инвестора - Майкл и Иван хотят вложиться в стартап.
Фаундеры сказали, что минимальная сумма инвестиций - X долларов, больше инвестировать можно сколько угодно.
У Майкла A долларов, у Ивана B долларов. Если оба могут вложиться - выведите 2, если только Майкл - Mike,
если только Иван - Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0
"""

min_sum = int(input('Введите минимальную сумму инвестиций: '))
mike_money = int(input('Введите сумму Майкла: '))
ivan_money = int(input('Введите сумму Ивана: '))

if mike_money >= min_sum and ivan_money >= min_sum:
    print(2)
elif mike_money >= min_sum >= ivan_money:
    print('Mike')
elif ivan_money >= min_sum >= mike_money:
    print('Ivan')
elif mike_money + ivan_money >= min_sum:
    print(1)

else:
    print(0)
