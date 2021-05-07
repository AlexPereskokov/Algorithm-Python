f_num = int(input(' Введите первое число: '))
s_num = int(input(' Введите второе число: '))
t_num = int(input(' Введите третье число: '))
if f_num < s_num < t_num or t_num < s_num < f_num:
    print(f'Cредним числом чисел: {f_num} {s_num} {t_num} является {s_num}')
elif f_num < t_num < s_num or s_num < t_num < f_num:
    print(f'Cредним числом чисел: {f_num} {s_num} {t_num} является {t_num}')
elif f_num == s_num or f_num == t_num or t_num == s_num:
    print(f'Cреди чисел: {f_num} {s_num} {t_num} нет среднего числа')
else:
    print(f'Cредним числом чисел: {f_num} {s_num} {t_num} является {f_num}')
