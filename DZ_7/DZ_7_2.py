# Произведём сортировку слиянием по возрастянию
# Введём функцию слияния, составляющую нам массив отсортированный
# И функцию мержа, позволяющую разрезать массив на части, которые и надо сравнивать
# Всё работает рекурсивно, функция мёржа обращается к функции слияния
# 39 строка соответсвует условию, для наглядности и красоты взяли элементы до 3 знака
import random


# функция слияния двух отсортированных списков
def merge_list(l_p, r_p):
    sort_mas = []
    i = 0
    j = 0
    while i < len(l_p) and j < len(r_p):
        if l_p[i] <= r_p[j]:
            sort_mas.append(l_p[i])
            i += 1
        else:
            sort_mas.append(r_p[j])
            j += 1
    sort_mas += l_p[i:] + r_p[j:]
    print(f' Промежуточный собираемый массив {sort_mas}')
    return sort_mas


# функция деления списка и слияния списков в общий отсортированный список
def split_and_merge_list(array):
    _mid = len(array) // 2
    left_part = array[:_mid]
    right_part = array[_mid:]
    print(f' Левая часть массива {left_part} \n'
          f' Правая часть массива {right_part}')
    if len(left_part) > 1:
        left_part = split_and_merge_list(left_part)
    if len(right_part) > 1:
        right_part = split_and_merge_list(right_part)
    return merge_list(left_part, right_part)


rand_mas = [float(format(random.uniform(0, 49.999), '.3f')) for _ in range(10)]
print(f' Исходный сгенерированный массив {rand_mas}')
print(f' Отсортированный массив {split_and_merge_list(rand_mas)}')
