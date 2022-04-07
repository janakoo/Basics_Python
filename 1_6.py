a = float(input ('Введите километраж за день: '))
b = float(input ('Цель: '))
i = 1
if a < b:
    while a < b:
       a = a*1.1
       i = i + 1
print('Day: ', i)
