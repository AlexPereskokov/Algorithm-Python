import random

print(' Привет, пользователь, поиграем в рандом! ')
f_int_range = int(input(' Начнём с целых чисел \n Введи первую границу: '))
s_int_range = int(input(' Введи вторую границу: '))
print(f' *** Рандом выбрал число *** : {random.randint(f_int_range, s_int_range)} ')
f_float_range = float(input(' Теперь вещественные числа \n Введи первую границу: '))
s_float_range = float(input(' Введи вторую границу: '))
print(f' *** Рандом выбрал число *** : {random.uniform(f_float_range, s_float_range)} ')
f_letter = ord(input(' И наконец, алфавит \n Введи первую границу: '))
s_letter = ord(input(' Введи вторую границу: '))
print(f' *** Рандом выбрал букву *** : {chr(random.randint(f_letter, s_letter))} ')
