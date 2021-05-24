# Данная задача проще исследуется в сети интернет, к счастью
# Первые два класса образуют структуру информации и листьев дерева
# Основная логика представлена в центральной функции (huff)
# Считывание и обращение к центральной функции реализовано в функции main
import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):

        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):

        code[self.char] = acc or '0'


def huff_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')
    return code

# Декодирование исходной строки обратно
# def huff_decode(encode, code):
#     sx = []
#     enc_ch = ''
#     for ch in encode:
#         enc_ch += ch
#         for dec_ch in code:
#             if code.get(dec_ch) == enc_ch:
#                 sx.append(dec_ch)
#                 enc_ch = ''
#                 break
#     return ''.join(sx)


def main(words):
    s = words
    code = huff_encode(s)
    encode = ''.join(code[ch] for ch in s)
    print(f' Число повторящихся символов - {len(code)}')
    for ch in sorted(code):
        print('{}: {}'.format(ch, code[ch]))
    print(encode)


test_str = input(' Введите строку из трёх слов: ')
main(test_str)

# P.S  Хотел сказать спасибо, Иван, за Ваши уроки, потраченное время и вложенный опыт!
