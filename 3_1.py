def first_func(var_1, var_2):
    return var_1 / var_2

A = float(input('1 ое число: '))
while True:
    try:
        print("Ответ: ", first_func(A, float(input('2 ое число: '))))
        break
    except ZeroDivisionError:  print("делить на ноль нельзя")