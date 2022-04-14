def first_func():
    a = int(input('Введите первое число:'))
    b = int(input('Введите второе число:'))
    if b == 0:
        while b == 0:
            print("Делить на ноль нельзя!")
            b = float(input("Введите второе число:"))
            break
    answer = a / b
    return answer
answer = first_func()
print("Ответ:", answer)