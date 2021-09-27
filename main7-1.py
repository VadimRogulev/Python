"""
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, 
заданный случайными числами на промежутке [-100; 100]. Выведите на экран исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее)
"""


import random


def bubble_sort(array_of_values):
    n = 1
    while n < len(array_of_values):
        count = 0
        for i in range(len(array_of_values) - 1 - (n - 1)):
            if array_of_values[i] < array_of_values[i + 1]:
                array_of_values[i], array_of_values[i + 1] = array_of_values[i + 1], array_of_values[i]
                count += 1
        if count == 0:
            break
        n += 1


array = [random.randint(-100, 100) for i in range(10)]

print('Массив:', array, sep='\n')
bubble_sort(array)
print('После сортировки:', array, sep='\n')
