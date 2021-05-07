# прогоняем все числа диапазона по делителям, выводим на последнем числе диапазона
min_item = 2
max_item = 99
f_div = 2
l_div = 9
array = [_ for _ in range(min_item, max_item + 1)]
divisor = [_ for _ in range(f_div, l_div + 1)]
for i in divisor:
    sum = 0
    for j in array:
        if j % i == 0:
            sum += 1
        if j == max_item:
            print(f' Из выбранного диапазона {min_item} - {max_item} : {sum} чисел кратны {i} ')
