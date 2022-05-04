class Store:
    def __init__(self):
        self._dict = {}

    def add_to_store(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)

    def manual_add_to_store(self):
        while True:
            st = input(f'Ввод принтера - p, сканера - s, копира - х,  выход - q: ')


            if st == 'P' or st == 'p'or st == 's' or st == 'S' or st == 'x' or st == 'X':
                name = input("Введите имя ")
                make = input("Введите страну-изготовитель ")
                try:
                    year = int(input("Введите год изготовления "))
                except ValueError:
                   print('Введите дату ')


                if  st == 'p' or st == 'P':
                    series = input("Введите серию ")
                    try:
                        zvet = int(input("1 - цветной, 0 - нет: "))
                    except ValueError:
                        print('1 или 0 !')

                    store.add_to_store(Printer(name, make, year, series, zvet))

                if st == 's' or st == 'S':
                    store.add_to_store(Scaner(name, make, year))
                if st == 'x' or st == 'X':
                    store.add_to_store(Xerox(name, make, year))


            else:
                break
            print('')


class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

class Printer(Equipment):
    def __init__(self, name, make, year, series, zvet):
        super().__init__(name, make, year)
        self.series = series
        self.zvet = zvet

    def __repr__(self):
        return f'{self.name} {self.make} {self.year} {self.series} {self.zvet}'


class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)


    def __repr__(self):
        return f'{self.name} {self.make} {self.year}'



class Xerox(Store):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def __repr__(self):
        return f'{self.name} {self.make} {self.year}'


store = Store()
print(store.manual_add_to_store())

print(store._dict)



