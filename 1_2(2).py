a = input('Введите время в сек: ')
sec = int(a)
print('время в секундах: ', sec)
sec = sec % (24*3600)
hour = sec // 3600
sec %= 3600
minute = sec // 60
sec %= 60
print(f'на часах {hour:02d} : {minute:02d} : {sec:02d}')