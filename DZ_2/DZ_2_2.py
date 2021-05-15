# простой вариант, по нему сделано блок-схема
def even_odd():
    num = input(' Введите Ваше число: ')
    if len(num) % 2 == 0:
        even = len(num) // 2
        odd = even
    else:
        even = len(num) // 2
        odd = even + 1
    return f' Количество чётных цифр: {even} \n Количество нечётных цифр: {odd}'


# ещё один вариант в цикл, , без len()
def even_odd_2():
    num = input(' Введите Ваше число: ')
    even = 0
    odd = 0
    for i, let in enumerate(num):
        i += 1
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return f' Количество чётных цифр: {even} \n Количество нечётных цифр: {odd}'


print(even_odd())
print(even_odd_2())
