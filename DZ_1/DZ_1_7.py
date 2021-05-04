# ищем неравенство треугольника и следующие условия
# будем считать стороны целыми числами
f_side = int(input(' Введите первую сторону треугольника: '))
s_side = int(input(' Введите вторую сторону треугольника: '))
t_side = int(input(' Введите третью сторону треугольника: '))
if f_side == s_side == t_side:
    print(f'Треугольник со сторонам {f_side} {s_side} {t_side} является равносторонним ')
elif f_side == s_side or s_side == t_side or t_side == f_side:
    print(f'Треугольник со сторонам {f_side} {s_side} {t_side} является равнобедренным ')
elif not(f_side + s_side > t_side) or not(f_side + t_side > s_side) or not(t_side + s_side > f_side):
    print(f'Треугольник со сторонам {f_side} {s_side} {t_side} невозможно построить по неравенству треугольника ')
else:
    print(f'Треугольник со сторонам {f_side} {s_side} {t_side} является разносторонним ')
