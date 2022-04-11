month = int(input('Введите месяц в виде числа:'))
seasone_list = ["Зима", "Весна", "Лето", "Осень"]
if month == 1 or month == 2 or month == 12:
    print(seasone_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasone_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasone_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasone_list[3])
else:
    print("Такой месяц не существует")