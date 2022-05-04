class MyExept(Exception):
    def __init__(self,txt):
        self.txt = txt


def div(a, b):
    try:
        if b == 0:
            raise MyExept("Делить на ноль нельзя!")
            return ''
        else:
            print("Программа завершена")
            return a / b
    except MyExept as err:
        return err


a1 = float(input("Введите делимое:"))
b1 = float(input("Введите делитель:"))
print(div(a1,b1))