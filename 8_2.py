class MyExept:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def div(a,b):
        try:
            res=a/b
        except:
            if b ==0:
                print("Деление на ноль недопустимо")
        else:
            print(f"Все хорошо. Результат = {res}")
        finally:
            print("Программа завершена")
        return ''

a1 = float(input("Введите делимое:"))
b1 = float(input("Введите делитель:"))
print(MyExept.div(a1,b1))