month = int(input('Введите месяц в виде числа:'))
seasone_dict = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}
if month == 1 or month == 2 or month == 12:
    print(seasone_dict[1])
elif month == 3 or month == 4 or month == 5:
    print(seasone_dict[2])
elif month == 6 or month == 7 or month == 8:
    print(seasone_dict[3])
elif month == 9 or month == 10 or month == 11:
    print(seasone_dict[4])
else:
    print("Такой месяц не существует")