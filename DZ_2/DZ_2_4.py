def sum_elem():
    print(' Имеется послежовательность чисел {1; -0.5; 0.25; -0.125} \n'
          ' Программа расчитывает сумму элементов данной последовательности')
    n = int(input(' Введите количество элементов последовательности: '))
    sum = 0
    seq_num = 1
    counter = 0
    while counter != n:
        sum += seq_num
        seq_num = (seq_num / 2) * (-1)
        counter += 1
    return sum


print(sum_elem())
