"""
2.Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

use_signs = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 0: '0', 1: '1', 2: '2',
             3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
             12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def sum_signs(x, y):
    result = deque()
    transfer = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)

    while x:
        if y:
            res = use_signs[x.pop()] + use_signs[y.pop()] + transfer
        else:
            res = use_signs[x.pop()] + transfer
        transfer = 0
        if res < 16:
            result.appendleft(use_signs[res])
        else:
            result.appendleft(use_signs[res - 16])
            transfer = 1
    if transfer:
        result.appendleft('1')

    return list(result)


def mul_signs(x, y):
    result = deque()
    spam = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = use_signs[y.pop()]
        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * use_signs[x[j]])
        for _ in range(i):
            spam[i].append(0)

    transfer = 0

    for _ in range(len(spam[-1])):
        res = transfer
        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()
        if res < 16:
            result.appendleft(use_signs[res])
        else:
            result.appendleft(use_signs[res % 16])
            transfer = res // 16
    if transfer:
        result.appendleft(use_signs[transfer])

    return list(result)


a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
b = list(input('Введите 2-е шестнадцатиричное число: ').upper())

print(*a, '+', *b, '=', *sum_signs(a, b))
print(*a, '*', *b, '=', *mul_signs(a, b))
