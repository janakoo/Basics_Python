def second_func(a1, a2, a3):
    if a1 <= a2 and a1 < a3 :
        return a2 + a3
    if a2 <= a1 and a2 < a3 :
        return a1 + a3
    else:
         return a1 + a2

V = [0, 0, 0]
while True:
   try:
     for i in range(3): V[i]=float(input('число n:'))
     break
   except ValueError:  print("Введите число")


print('Сумма наибольших чисел:', second_func(V[0],V[1],V[2]))