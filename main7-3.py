"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
то используйте метод сортировки, который не рассматривался на уроках
"""



def select(array_of_values, left_side, right_side, n):
    while True:
        if left_side == right_side:
            return left_side

        pivotIndex = pivot(array_of_values, left_side, right_side)
        pivotIndex = partition(array_of_values, left_side, right_side, pivotIndex, n)
        if n == pivotIndex:
            return n
        elif n < pivotIndex:
            right_side = pivotIndex - 1
        else:
            left_side = pivotIndex + 1


def partition(array_of_values, left_side, right_side, pivot_index, n):
    pivot_value = array_of_values[pivot_index]
    store_index = left_side

    for i in range(left_side, right_side - 1):
        if array_of_values[i] < pivot_value:
            array_of_values[store_index], array_of_values[i] = array_of_values[i], array_of_values[store_index]
            store_index += 1
    store_index_eq = store_index
    for i in range(store_index, right_side - 1):
        if array_of_values[i] == pivot_value:
            array_of_values[store_index_eq], array_of_values[i] = array_of_values[i], array_of_values[store_index]
            store_index_eq += 1
    array_of_values[right_side], array_of_values[store_index_eq] = array_of_values[store_index_eq], \
                                                                   array_of_values[right_side]

    if n < store_index:
        return store_index
    if n <= store_index_eq:
        return n
    return store_index_eq


def partition_5(array_of_values, left_side, right_side):
    i = left_side + 1
    while i <= right_side:
        j = i
        while j > left_side and array_of_values[j - 1] > array_of_values[j]:
            array_of_values[j - 1], array_of_values[j] = array_of_values[j], array_of_values[j - 1]
            j -= 1
        i += 1
    return (left_side + right_side) // 2


def pivot(array_of_values, left_side, right_side):
    if right_side - left_side < 5:
        return partition_5(array_of_values, left_side, right_side)

    for i in range(left_side, right_side, 5):
        sub_right = i + 4
        if sub_right > right_side:
            sub_right = right_side
        median_5 = partition_5(array_of_values, i, sub_right)
        array_of_values[median_5], array_of_values[left_side + (i - left_side) //
                                                   5] = array_of_values[left_side + (i - left_side) // 5], \
                                                        array_of_values[median_5]

    mid = (right_side - left_side) / 10 + left_side + 1
    return select(array_of_values, left_side, left_side + (right_side - left_side) // 5, mid)


if __name__ == '__main__':
    m = 6
    array_of_values = [10, 90, 31, 96, 74, 56, 7, 11, 91, 73, 86, 62, 22]
    print(array_of_values)

    left_side = 0
    right_side = len(array_of_values) - 1
    med_ind = pivot(array_of_values, left_side, right_side)

    print(f'медиана массива: {array_of_values[med_ind]}')
    print(sorted(array_of_values))
