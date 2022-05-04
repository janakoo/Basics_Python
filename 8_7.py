class MyComplex():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return (f'{self.a} + {self.b}*i')


    def __add__(self, other):
        return MyComplex(self.a+other.a,self.b+other.b)

    def __mul__(self, other):
        return MyComplex(self.a * other.a - self.b*other.b, self.a * other.b + self.b * other.a)

m1 = MyComplex(1,1)
m2 = MyComplex(2,2)
print('Сумма двух чисел: ',m1+m2)
print('Произведение двух чисел: ',m1*m2)
