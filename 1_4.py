a = input('Введите целое положительное число: ')
b = int(a)
m = b % 10
while b >= 1:
    b = b // 10
    if b % 10 > m:
        m = b % 10
    elif b > 9:
        continue
    else:
        print("Максимальная цифра в числе ", m)
        break
