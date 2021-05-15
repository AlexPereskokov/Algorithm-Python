# второй минимальный элемент - предыдущий минимальный
import random

size = 10
mim_item = 1
max_item = 100
array = [random.randint(mim_item, max_item) for _ in range(size)]
f_min_el = max_item
s_min_el = max_item
for ind, el in enumerate(array):
    if el < f_min_el:
        f_min_el, s_min_el = el, f_min_el
    elif el <= s_min_el:
        s_min_el = el
print(f' Сгенерированный массив элементов: {array} \n'
      f' Минимальные элементы массива : {f_min_el} и {s_min_el}')
