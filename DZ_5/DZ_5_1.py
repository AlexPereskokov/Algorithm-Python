# использованы разные типы коллекций,(обычный словарь) и deque
# сделана проверка на ненулевое значение числа компаний, 3 попытки дать ненулевое значение...
# сделана проверка на неповторяющиеся названия компаний, миллиард попыток
# проверки сделаны циклами, без try/except, хотя наверное так не совсем корректно, но захотелось поиграть с циклами
# сделан вывод таким образом, чтобы пустых строк не было, вместо них выводятся уникальные строки (нет таких компаний)
import collections
import sys

companies = collections.defaultdict()
prof_c = collections.deque()
midprof_c = collections.deque()
unprof_c = collections.deque()
all_prof = 0
quarter = 4
anger = 0
num_of_business = int(input(' Введите количество предприятий: '))
while num_of_business == 0:
    if anger == 2:
        print(' Шутки кончились...Всего доброго!')
        sys.exit()
    num_of_business = int(input(' Серьёзно? Ноль компаний? А зачем я вообще писал этот код? \n'
                                ' Введите количество предприятий ещё раз: '))
    anger += 1
for bs in range(num_of_business):
    bs += 1
    name = input(f' Введите название {bs} компании: ')
    while name in companies.keys():
        name = input(f' Недопустимо повторение названий компаний! \n'
                     f' Введите другое название {bs} компании, пожалуйста...: ')
    prof = 0
    for pr in range(quarter):
        pr += 1
        prof += float(input(f' Введите прибыль за {pr} квартал: '))
        if pr == 4:
            companies[name] = prof
            all_prof += prof
            print(f' Общая прибыль компании {bs} составила: {prof}')
mid_prof = all_prof / num_of_business
for i, com_prf in companies.items():
    if com_prf > mid_prof:
        prof_c.append(i)
    elif com_prf == mid_prof:
        midprof_c.append(i)
    else:
        unprof_c.append(i)
print(f' Средняя прибыль всех компаний: {mid_prof}')
if len(prof_c) != 0:
    print(f' \n Прибыль выше среднего достигли компании: ', end='')
    for nm in prof_c:
        print(nm, ' ', end='')
else:
    print('\n Компаний, имеющих прибыль выше среднего, нет')
if len(midprof_c) != 0:
    print(f' \n Прибыль на уровне среднего достигли компании: ', end='')
    for nm in midprof_c:
        print(nm, ', ', end='')
else:
    print('\n Компаний, имеющих прибыль на уровне среднего, нет', end= '')
if len(unprof_c) != 0:
    print(f' \n Прибыль ниже среднего достигли компании: ', end='')
    for nm in unprof_c:
        print(nm, ' ', end='')
else:
    print('\n Компаний, имеющих прибыль ниже среднего, нет')
