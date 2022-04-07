a = input('Введите время в сек: ')
sec = int(a)
print('время в секундах: ', sec)
sec = sec % (24*3600)
hour = sec // 3600
sec %= 3600
minute = sec // 60
sec %= 60
print('%02d: %02d: %02d' % (hour, minute, sec))