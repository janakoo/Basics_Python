goods = []
features = {'наименование': '', 'цена': '', 'количество': '', 'единицы': ''}
analytics = {'наименование': [], 'цена': [], 'количество': [], 'единицы': []}
num = 0
while True:
    control = input(
        "Для выхода из программы (и показа готовой структуры) нажмите 'Q', продолжить ввод товаров 'Enter', для анализа нажать 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print('\n Анализ. Текущее состояние: \n')

        for key, value in analytics.items():
            print(f'{key}: {value}')
    for f in features.keys():
        feature_ = input(f'Введите характеристики "{f}":')
        features[f] = int(feature_) if (f == 'цена' or f == 'количество') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))

print('\n Окончательный список товаров: \n')
for key, value in analytics.items():
    print(f'{key}: {value}')

print('-' * 30)
print(goods)