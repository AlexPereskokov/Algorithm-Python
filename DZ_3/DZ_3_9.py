# заполним матрицу
import random

row = 5
column = 5
min_item = 1
max_item = 10
double_mas = [[random.randint(min_item, max_item) for _ in range(row)] for i in range(column)]
# выведем её
print(' Наша сгенерированная матрица : ')
for i in range(column):
    print(' ', double_mas[i])
# заполним массив минимальных элементов каждого столбца матрицы
min_mas_column = []
for col in range(column):
    min_el = max_item
    for r in range(row):
        if double_mas[r][col] < min_el:
            min_el = double_mas[r][col]
        if r == row - 1:
            min_mas_column.append(min_el)
print(f' Массив минимальных элементов каждого столбца матрицы : {min_mas_column}')
# найдём из минимальных элементов столбцов максимальный по матрице
max_el = min_item
for el in min_mas_column:
    if el > max_el:
        max_el = el
print(f' Искомый макисмум матрицы из минимумов по столбцам : {max_el}')
