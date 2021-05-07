import random


def guess():
    print(' Данная программа даёт возможность угадать число в диапазоне {1;100} \n'
          ' У Вас есть 10 попыток, так начнём же!')
    guess_num = random.randint(1, 100)
    for i in range(1, 11):
        user_num = int(input(' Введите число: '))
        if user_num > guess_num:
            print(f' Загаданное число меньше \n Осталось {10 - i} попыток')
        elif user_num < guess_num:
            print(f' Загаданное число больше \n Осталось {10 - i} попыток')
        else:
            return ' !!! Вы угадали !!! '
    return f' ...Вы не уложились за 10 попыток... \n Загаданное число равнялось {guess_num}'


print(guess())
