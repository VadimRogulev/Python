"""
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

from collections import Counter, deque


class Separation:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def huffmans_algorithm(input_string):
    counter = Counter(input_string)
    deq = deque(sorted(counter.items(), key=lambda x: x[1]))
    while len(deq) > 1:
        weight = deq[0][1] + deq[1][1]
        location = Separation(left=deq.popleft()[0], right=deq.popleft()[0])
        for index, item in enumerate(deq):
            if weight > item[1]:
                continue
            else:
                deq.insert(index, (location, weight))
                break
        else:
            deq.append((location, weight))
    return deq[0][0]


def encode(tree, encode_table, path=''):
    if not isinstance(tree, Separation):
        encode_table[tree] = path
    else:
        encode(tree=tree.left,  encode_table=encode_table, path=f'{path}0')
        encode(tree=tree.right, encode_table=encode_table, path=f'{path}1')


some_string = 'soft french buns'
encode_dict = dict()
encode(huffmans_algorithm(some_string), encode_dict)
encoded_list = []

for element in some_string:
    encoded_list.append(encode_dict[element])
encoded_string = ''.join(encoded_list)

print(f'Оригинальная строка:   {some_string}')
print(f'Закодированная строка: {encoded_string}')
