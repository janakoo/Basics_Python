class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)
    def __sub__(self, other):
        if int((self.count)) - int((other.count)) >0:
            return Cell(int((self.count)) - int((other.count)))
        else:
            return f'Вычитание не возможно'
    def __mul__(self, other):
        return Cell(self.count * other.count)
    def __truediv__(self, other):
        if other.count!= 0:
            return Cell(int(self.count / other.count))
        else:
            return f'Делить на ноль нельзя'
    def __str__(self):
        return f"Объект с параметрами {self.count}"

    def make_order(self,row):
        for i in range(self.count// row ):
            print(row*'🐭 ')
        print(self.count%row*'🐭 ')
        return ''




mc1 = Cell(21)
mc2 = Cell(10)

print("1. сумма")
print(mc1 + mc2)
print("2. разность")
print(mc1 - mc2)
print("3. умножение")
print(mc1 * mc2)
print("4. деление")
print(mc1 / mc2)
print("5. make order")
print(mc1.make_order(5))
