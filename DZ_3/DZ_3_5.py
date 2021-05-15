# сделана простая проверка на генерируемый массив, при положительном массива индекс не изменится с -1
import random

size = 10
mim_item = -50
max_item = 50
array = [random.randint(mim_item, max_item) for _ in range(size)]
max_neg_item = mim_item
max_neg_ind = -1
for ind, item in enumerate(array):
    if item < 0 and abs(item) < abs(max_neg_item):
        max_neg_item = item
        max_neg_ind = ind
print(f' Сгенерированный массив элементов: {array}')
if max_neg_ind != -1:
    print(f' Найден максимальный отрицательный элемент \n'
          f' Его значение : {max_neg_item} \n Его индекс : {max_neg_ind}')
else:
    print(' Данный массив не имеет отрицательных чисел')
