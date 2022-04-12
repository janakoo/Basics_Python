value = [int(i) for i in input('Введите значения через пробел: ').split()]
print(value)
for i in range (0,len(value)//2*2,2):
    value[i+1],value[i] = value[i],value[i+1]
print(value)
