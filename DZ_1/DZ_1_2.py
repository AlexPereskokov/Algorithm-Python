f_num = 5
s_num = 6
print(f' Битовое представление числа {f_num} = {bin(f_num)}')
print(f' Битовое представление числа {s_num} = {bin(s_num)}')
print(f' Логическое "И" чисел: {f_num} & {s_num} = {bin(f_num & s_num)}')
print(f' Логическое "ИЛИ" чисел: {f_num} | {s_num} = {bin(f_num | s_num)}')
print(f' Исключающее "ИЛИ" чисел: {f_num} ^ {s_num} = {bin(f_num ^ s_num)}')
print(f' Сдвиг числа {f_num} влево на 2 знака: {f_num} << 2 = {bin(f_num << 2)}')
print(f' Сдвиг числа {f_num} вправо на 2 знака: {f_num} >> 2 = {bin(f_num >> 2)}')
# При битовом сдвиге биты сдвигаются на указанное кол-во ячеек, в свободные ячейки (0/1)
