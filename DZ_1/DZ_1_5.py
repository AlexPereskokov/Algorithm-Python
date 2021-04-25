f_letter = ord(input(' Введите первую букву: '))
s_letter = ord(input(' Введите вторую букву: '))
# изменим переменные Unicode, в соответствии с порядком алфавита
f_letter -= ord('a') - 1
s_letter -= ord('a') - 1
if f_letter == s_letter or abs(s_letter - f_letter) == 1:
    count_letter_between = 0
else:
    count_letter_between = abs(s_letter - f_letter) - 1
print(f' Место первой буквы алфавита: {f_letter} \n'
      f' Место второй буквы алфавита: {s_letter} \n'
      f' Колличество букв между выбранными: {count_letter_between}')
