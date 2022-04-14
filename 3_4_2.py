def second_func(x,y):
    t = 1/x
    for i in range(0, -y-1):
        t = t/x
    return t

a = float(input('Введите первое число:'))
while True:
    b = int(input('Введите второе (отрицательное целое) число:'))
    if b < 0:
        print("Ответ: ", second_func(a,b))
        break