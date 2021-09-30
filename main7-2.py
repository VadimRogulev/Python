"""
2.Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50]. Выведите на экран исходный и отсортированный массивы.
"""


import random


def merge_sort(array_of_values):
    if len(array_of_values) <= 1:
        return array_of_values

    left = merge_sort(array_of_values[:len(array_of_values) // 2])
    right = merge_sort(array_of_values[len(array_of_values) // 2:])
    i, j = 0, 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            array_of_values[i + j] = left[i]
            i += 1
        else:
            array_of_values[i + j] = right[j]
            j += 1

    while len(left) > i:
        array_of_values[i + j] = left[i]
        i += 1
    while len(right) > j:
        array_of_values[i + j] = right[j]
        j += 1

    return array_of_values


array = [random.uniform(0, 50) for i in range(10)]

print('Массив:', array, sep='\n')
merge_sort(array)
print('После сортировки:', array, sep='\n')
