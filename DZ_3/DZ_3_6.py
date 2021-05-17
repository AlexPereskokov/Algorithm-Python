import random

size = 10
mim_item = 1
max_item = 100
array = [random.randint(mim_item, max_item) for _ in range(size)]
max_el = mim_item
min_el = max_item
min_ind = 0
max_ind = 0
sum_btw_max_min = 0
for ind, item in enumerate(array):
    if item > max_el:
        max_el = item
        max_ind = ind
    if item < min_el:
        min_el = item
        min_ind = ind
# условие для перебора в разные стороны, без смены индексов
if min_ind > max_ind:
    max_ind, min_ind = min_ind, max_ind
for el in range(min_ind + 1, max_ind):
    sum_btw_max_min += array[el]
print(f' Сгенерированный массив элементов: {array} \n'
      f' Максимальный элемент массива : {max_el} \n'
      f' Минимальный элемент массива : {min_el} \n'
      f' Сумма между этими элементами : {sum_btw_max_min}')
