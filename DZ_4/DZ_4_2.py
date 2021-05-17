import math
import timeit
import cProfile


# 1 способ. Используем Решето Эратосфена
def erat(num):
    simple_lst = [i for i in range(2, 3572)]
    for i in range(2, 3572):
        for el in simple_lst:
            if el != i and el % i == 0:
                simple_lst.remove(el)
    return simple_lst[num - 1]


# Проверка времени работы
# print(timeit.timeit(f'{erat(5)}', number=100, globals=globals()))       # 2.500000000016378e-06
# print(timeit.timeit(f'{erat(50)}', number=100, globals=globals()))      # 1.600000000046009e-06
# print(timeit.timeit(f'{erat(500)}', number=100, globals=globals()))     # 1.600000000046009e-06
# Профайлер
# cProfile.run('erat(5)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1         0.000    0.000    0.181    0.181 <string>:1(<module>)
# 1         0.154    0.154    0.181    0.181 DZ_4_2.py:7(erat)
# 1         0.000    0.000    0.000    0.000 DZ_4_2.py:8(<listcomp>)
# 1         0.000    0.000    0.181    0.181 {built-in method builtins.exec}
# 1         0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 3070      0.027    0.000    0.027    0.000 {method 'remove' of 'list' objects}

# cProfile.run('erat(50)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1         0.000    0.000    0.206    0.206 <string>:1(<module>)
# 1         0.173    0.173    0.206    0.206 DZ_4_2.py:7(erat)
# 1         0.000    0.000    0.000    0.000 DZ_4_2.py:8(<listcomp>)
# 1         0.000    0.000    0.206    0.206 {built-in method builtins.exec}
# 1         0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 3070      0.032    0.000    0.032    0.000 {method 'remove' of 'list' objects}

# cProfile.run('erat(500)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1         0.000    0.000    0.197    0.197 <string>:1(<module>)
# 1         0.169    0.169    0.197    0.197 DZ_4_2.py:7(erat)
# 1         0.000    0.000    0.000    0.000 DZ_4_2.py:8(<listcomp>)
# 1         0.000    0.000    0.197    0.197 {built-in method builtins.exec}
# 1         0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 3070      0.028    0.000    0.028    0.000 {method 'remove' of 'list' objects}


# 2 способ. Алгоритм без использования Решета, добавление корня
def simple(num):
    simple_lst = []
    for i in range(2, 3572):
        if num == len(simple_lst):
            return simple_lst[num - 1]
        for j in range(2, 1 + int(math.sqrt(i))):
            if not i % j:
                break
        else:
            simple_lst.append(i)


# Проверка времени работы
# print(timeit.timeit(f'{simple(5)}', number=100, globals=globals()))       # 3.0000000000030003e-06
# print(timeit.timeit(f'{simple(50)}', number=100, globals=globals()))      # 1.299999999995749e-06
# print(timeit.timeit(f'{simple(500)}', number=100, globals=globals()))     # 1.3999999999986246e-06
# Профайлер

# cProfile.run('simple(5)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1         0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1         0.000    0.000    0.000    0.000 DZ_4_2.py:50(simple)
# 1         0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 11        0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 10        0.000    0.000    0.000    0.000 {built-in method math.sqrt}
# 5         0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 1         0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('simple(50)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1         0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1         0.000    0.000    0.000    0.000 DZ_4_2.py:50(simple)
# 1         0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 229       0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 228       0.000    0.000    0.000    0.000 {built-in method math.sqrt}
# 50        0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 1         0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('simple(500)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1         0.000    0.000    0.005    0.005 <string>:1(<module>)
# 1         0.004    0.004    0.005    0.005 DZ_4_2.py:50(simple)
# 1         0.000    0.000    0.005    0.005 {built-in method builtins.exec}
# 3570      0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 3570      0.001    0.000    0.001    0.000 {built-in method math.sqrt}
# 500       0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 1         0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Проработка проверки функций
def test_revers(func):
    _lst = [2, 3, 5, 7, 11]
    for i, item in enumerate(_lst):
        i += 1
        assert func(i) == item, f' Ошибка {i}'
        print(f' Test {i} OK')


# test_revers(erat)
# test_revers(simple)

# Вывод: классический алгоритм Эратосфена проигрывает в скорости
# Дело в том, что 1 способ нацелен на вычленение нужных элементов
# Тогда как 2 способ заполняет новый массив нужными, и может быть прерван по i-ому элементу
# 1 способ можно улучшить, несмотря на то, что он также быстр, но тогда это не будет классическим Решетом
# Оба способа достаточно быстродейственны и просты в использовании
# По timeit они сравнивают скорость к последнему элементу, а по сProfile 1 уступает в скорости
