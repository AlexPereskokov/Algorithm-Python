# меняем size для наглядности работы (10 - 200)
import random

size = 50
mim_item = 1
max_item = 100
array = [random.randint(mim_item, max_item) for _ in range(size)]
repeat_num = 1
repeat_item = 0
for i in array:
    if array.count(i) > repeat_num:
        repeat_num = array.count(i)
        repeat_item = i
print(f' Сгенерированный массив элементов: \n {array}')
if repeat_item != 0 and [2, 3, 4].count(repeat_num) != 1:
    print(f' Число сгенерированного массива {repeat_item} повторяется {array.count(repeat_item)} раз')
elif repeat_item != 0 and [2, 3, 4].count(repeat_num) == 1:
    print(f' Число сгенерированного массива {repeat_item} повторяется {array.count(repeat_item)} разa')
else:
    print(' Сгенерированный массив не имеет повторяющихся элементов')
