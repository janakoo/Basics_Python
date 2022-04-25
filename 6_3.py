class Worker:
    def __init__(self, name, surname, position, wage,bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' +self.surname

    def get_total_income(self):
        return sum(self._income.values())


person = Position('Ivan', 'Ivanov','manager',1200, 500)
person2 = Position('Petr', 'Petrov','IT manager',1300, 600)



print(person.get_full_name(), person.get_total_income())
print(person2.get_full_name(), person2.get_total_income())