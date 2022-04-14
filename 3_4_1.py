def second_func(x,y):
  return x**y

a = float(input('Введите первое число:'))
while True:
    b = int(input('Введите второе (отрицательное целое) число:'))
    if b < 0:
        print("Ответ: ", second_func(a,b))
        break