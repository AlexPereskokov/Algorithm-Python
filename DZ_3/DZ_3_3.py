# при одинаковых значениях массива производится замена первой пары минимального и максимального элемента
import random

size = 10
mim_item = 1
max_item = 100
array = [random.randint(mim_item, max_item) for _ in range(size)]
print(f' Сгенерированный массив элементов: {array}')
max_el = mim_item
min_el = max_item
min_ind = 0
max_ind = 0
for ind, item in enumerate(array):
    if item > max_el:
        max_el = item
        max_ind = ind
    if item < min_el:
        min_el = item
        min_ind = ind
array[max_ind], array[min_ind] = array[min_ind], array[max_ind]
print(f' Изменённый сгенерированный массив элементов: {array}')
