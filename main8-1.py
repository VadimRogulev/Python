"""
1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
"""

import hashlib


def substring_calculation(input_string):
    input_string = str(input_string).lower()
    length_string = len(input_string)
    hash_set = set()

    for i in range(length_string + 1):
        for j in range(i + 1, length_string + 1):
            hash = hashlib.sha1(input_string[i:j].encode('utf-8')).hexdigest()
            hash_set.add(hash)
    return len(hash_set)


working_line = 'pineapple'

print(f'Количество различных подстрок в строке {working_line}: {substring_calculation(working_line)}')
