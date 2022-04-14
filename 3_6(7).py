def int_func(x):
    return x.title()


priznak = 0

while priznak == 0:
    word = input("Введите слова из маленьких латинских букв: ")
    if 1 in [(list(word))[i].isupper() == 1 or (list(word))[i].isdigit() == 1 for i in range(len(word))]:
        priznak = 0

    else:
        priznak = 1

print(int_func(word))