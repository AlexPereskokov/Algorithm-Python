# простой метод, но без использования встроенной функции(по нему будет б/с)
def revers():
    num = input(' Введите своё число: ')
    rev_num = 0
    cf = 0.1
    for i in num:
        cf *= 10
        part_num = int(i) * cf
        rev_num += part_num
    return int(rev_num)


# использую метод строк(мб читерство, но самый быстрый способ, не считая [::-1])
def revers_ed():
    num = input(' Введите своё число: ')
    rev_num = ''.join(reversed(num))
    return rev_num


print(revers())
print(revers_ed())
