"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import math

n = 900


def loop(border):
    num = 2
    i = 0
    while i != border:
        num = num * math.sqrt(num)
        i += 1
    print(f'Результат после {border} итераций равен {num} (Цикл)')


def recursion(i, num, border):
    if i == border:
        print(f'Результат после {i} итераций равен {num} (Рекурсия)')
        return num
    elif i <= border:
        return recursion(i + 1, num * math.sqrt(num), border)

# cp.run('loop(n)')

# Результат после 900 итераций равен inf (Цикл)
#          905 function calls in 0.001 seconds


# cp.run('recursion(0, 2, n)')

# Результат после 900 итераций равен inf (Рекурсия)
#          1805 function calls (905 primitive calls) in 0.004 seconds
