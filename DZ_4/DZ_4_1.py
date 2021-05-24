# Берём уже решённую нами задачу, а именно ДЗ 2.3(имеет функции, достаточно проста)

# Условие задачи следующее:
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

import timeit
import cProfile
import random


# 1 вариант. Складывание числа по цифрам
def revers_1(number):
    rev_num = 0
    _cf = 0.1
    for i in number:
        _cf *= 10
        part_num = int(i) * _cf
        rev_num += part_num
    return int(rev_num)


# Заполним специальный массив, для отработки timeit
str_lst = []
for _ in range(10):
    r = str(random.randint(1, 10000))
    str_lst.append(r)
for el in str_lst:
    print(timeit.timeit(f'{revers_1(el)}', number=100, globals=globals()))
# Порядок времени выполнения операций
#   2.4000000000135024e-06
#   2.299999999996749e-06
#   2.3999999999996247e-06
#   2.299999999996749e-06
num = input(' Введите своё число: ')
cProfile.run('revers_1(num)')
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 DZ_4_1.py:13(revers_1)
# 1    0.000    0.000    0.000    0.000 0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Алгоритм работает быстро, на любых значениях, в оптимизации не нуждается


# 2 вариант. Использование встроенной функции reversed()
def revers_2(number):
    rev_num = ''.join(reversed(number))
    return int(rev_num)


# Заполним специальный массив, для отработки timeit
# str_lst = []
# for _ in range(10):
#     r = str(random.randint(1, 10000))
#     str_lst.append(r)
# for el in str_lst:
#     print(timeit.timeit(f'{revers_2(el)}', number=100, globals=globals()))
# Порядок времени выполнения операций
#   1.3999999999986246e-06
#   1.3000000000096268e-06
#   1.1999999999928734e-06
#   1.299999999995749e-06
# num = input(' Введите своё число: ')
# cProfile.run('revers_2(num)')
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 DZ_4_1.py:44(revers_2)
# 1    0.000    0.000    0.000    0.000 0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 1    0.000    0.000    0.000    0.000 0.000 {method 'join' of 'str' objects}

# Алгоритм работает быстро, на любых значениях, в оптимизации не нуждается


# 3 варинт. Запрещённый ранее, убрать детей от экрана, обратный массив
def revers_3(number):
    rev_num = number[::-1]
    return int(rev_num)


# Заполним специальный массив, для отработки timeit
# str_lst = []
# for _ in range(10):
#     r = str(random.randint(1, 10000))
#     str_lst.append(r)
# for el in str_lst:
#     print(timeit.timeit(f'{revers_3(el)}', number=100, globals=globals()))
# Порядок времени выполнения операций
#   1.5000000000015001e-06
#   1.299999999995749e-06
#   1.299999999995749e-06
#   1.2000000000067512e-06
# num = input(' Введите своё число: ')
# cProfile.run('revers_3(num)')
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 DZ_4_1.py:72(revers_3)
# 1    0.000    0.000    0.000    0.000 0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Алгоритм работает быстро, на любых значениях, в оптимизации не нуждается


# Проработка проверки функций
def test_revers(func):
    _lst = ['123', '230', '0']
    _rev_lst = [321, 32, 0]
    for i, item in enumerate(_lst):
        assert func(item) == _rev_lst[i], f' Ошибка {i}'
        print(f' Test {i} OK')


# test_revers(revers_1)
# test_revers(revers_2)
# test_revers(revers_3)


# Вывод: 3 разных алгоритма работают на примерно равной скорости
# Самый быстрый естественно reversed(), ибо написал на ++
# Потом идёт разворот массива, тоже достаточно прост для расчётов
# И замыкает таблицу скоростей первый алгоритм, чисто математический
# По сложности алгоритмы также примерно равны, в разработке предпочтительно использовать второй
