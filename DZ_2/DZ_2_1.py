def calc():
    print('  Добро пожаловать в простейший калькулятор \n '
          ' Вы можете выполнить операции (+) (-) (/) (*) \n '
          ' Для выхода из калькулятора введите (0) в качестве оператора')
    while True:
        f_num = int(input(' Введите превое число: '))
        s_num = int(input(' Введите второе число: '))
        o = input(' Введите оператор: ')
        if o == '+':
            print(f' Сумма чисел равна {f_num + s_num}')
        elif o == '-':
            print(f' Разность чисел равна {f_num - s_num}')
        elif o == '/':
            try:
                f_num / s_num
            except ZeroDivisionError:
                print(' Деление на ноль недопустимо')
                continue
            print(f' Деление чисел равно {f_num / s_num}')
        elif o == '*':
            print(f' Произведение чисел равно {f_num * s_num}')
        elif o == '0':
            print(f' Всего доброго ')
            break
        else:
            print(' Ошибочный оператор, попробуйте снова')


calc()
