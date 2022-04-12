my_str = input('Введите свой текст:')
chunks = my_str.split( )
for ind,el in enumerate (chunks, 1):
    if len(el) <= 10:
        print(f"{ind}){el}")
    else:
        print(f"{ind}){el[0:10]}")
