my_list = [110, 18, 15, 13, 13, 12, 1]
print("Набор чисел:", my_list)
input_value = int(input('Введите натуральное число: '))

if input_value < 1:
    print(input_value, " не является натуральным числом")
else:
    length = len(my_list)
    if my_list[0] < input_value:
        my_list.insert(0, input_value)
    elif my_list[length - 1] > input_value:
        my_list.append(input_value)
    else:
        for i in range(length - 1):
            if my_list[i] > input_value and my_list[i + 1] <= input_value:
                my_list.insert(i + 1, input_value)

    print("Новый набор чисел:", my_list)
