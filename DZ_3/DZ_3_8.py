# Размерность матрицы варьируется переменной 'стоблец' и введенными данными
column = 5
double_mas = []
for i in range(column):
    value = input(' Введите строку: ')
    f_v = int(value[0])
    s_v = int(value[1])
    t_v = int(value[2])
    sum_v = f_v + s_v + t_v
    double_mas.append([f_v, s_v, t_v, sum_v])
print(' Искомая матрица выглядит так :')
for i in range(column):
    print(' ', double_mas[i])
