"""
3. В массиве случайных целых чисел поменять местами минимальный и
максимальный элементы.
"""

import random

r = [random.randint(0, 99) for _ in range(10)]
print(f'Массив до изменения: {r}')

max_element = r[0]
min_element = r[0]

for i in r:
    if i > max_element:
        max_element = i
    elif i < min_element:
        min_element = i
min_index = r.index(min_element)
max_index = r.index(max_element)
r[min_index], r[max_index] = r[max_index], r[min_index]
print(f'Массив осле изменения элементов {min_index} и {max_index}: {r}')