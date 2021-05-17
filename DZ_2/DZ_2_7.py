def left_part(n):
    if n == 1:
        return n
    else:
        return n + left_part(n-1)


def right_part(n):
    return n * (n + 1) // 2


# возьём три числа для проверки, можно сколько угодно
f_num = int(input(' Введите первое число: '))
s_num = int(input(' Введите второе число: '))
t_num = int(input(' Введите третье число: '))
for num in f_num, s_num, t_num:
    if left_part(num) == right_part(num):
        print(f' При проверки n = {num} Равенство выполняется ')
    else:
        print(f' Равенство некорректно на n = {num} ')
