# можно было дать пользователю заполнить первый массив, но задание по "вводу" не явное, сделал генерацию
import random

size = 10
mim_item = 1
max_item = 100
array = [random.randint(mim_item, max_item) for _ in range(size)]
new_mass = []
for ind, item in enumerate(array):
    if item % 2 == 0:
        new_mass.append(ind)
print(f' Сгенерированный массив элементов: {array} \n'
      f' Индексы чётных элементов сгенерированного массива {new_mass}')
