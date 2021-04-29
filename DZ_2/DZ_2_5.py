def asc():
    f_sym = 32
    l_sym = 127
    for i in range(f_sym, l_sym):
        print(i, '-', chr(i), ' ', end='')
        if (i-1) % 10 == 0:
            print()


asc()
