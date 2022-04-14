name = input('Введите имя:')
surname = input('Введите фамилию:')
year = int(input('Введите год рождения:'))
city = input('Введите город проживания:')
email = input('Введите email:')
telephone = input('Введите телефон:')


def user(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])

print(user(name, surname, str(year), city , email, telephone))