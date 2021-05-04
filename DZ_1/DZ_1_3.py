print(' Введите две координаты, данные вводятся через "." ')

''' # более простой и краткий вариант, но присутствует split()
y_f_dot, x_f_dot = input(' Введите координату первой точки: ').split('.')
y_s_dot, x_s_dot = input(' Введите координату второй точки: ').split('.')
k_ratio = (int(x_s_dot) - int(x_f_dot)) / (int(y_s_dot) - int(y_f_dot))
b_ratio = int(y_f_dot) - (k_ratio * int(x_f_dot))
'''

f_dot = float(input(' Введите координаты первой точки: '))
s_dot = float(input(' Введите координаты второй точки: '))
y_f_dot = int(f_dot // 1)
x_f_dot = int((f_dot * 10) % 10)
y_s_dot = int(s_dot // 1)
x_s_dot = int((s_dot * 10) % 10)
k_ratio = (x_s_dot - x_f_dot) / (y_s_dot - y_f_dot)
b_ratio = y_f_dot - k_ratio * x_f_dot
if b_ratio < 0:
    b_ratio *= -1
    print(f' Линейная функция имеет следующий вид: y = {k_ratio}x - {b_ratio} ')
elif b_ratio == 0:
    print(f' Линейная функция имеет следующий вид: y = {k_ratio}x ')
else:
    print(f' Линейная функция имеет следующий вид: y = {k_ratio}x + {b_ratio} ')
