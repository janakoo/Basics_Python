def summ_func(x):
    summ = 0
    for i in x:
        summ += i
    return summ


summ = 0
priznak = 1
print("Для выхода из программы и показа итоговой суммы нажмите 'q', для расчета текущей суммы Enter")
while priznak == 1:
    number = input("Введите числа через пробел:").split()
    if 'q' in number:
        del number[number.index('q'):len(number)]
        priznak = 0

    num = [int(i) for i in number]
    summ += summ_func(num)
    print(summ)

print("Ответ:", summ)