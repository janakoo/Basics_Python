from random import randint
outputfile = open("output5_5.txt", "w")

for i in range(randint(0, 100)):
    outputfile.write(str(randint(0, 100)) + ' ')
outputfile.close()

array = []
my_f = open("output5_5.txt", "r")

for line in my_f:
    array.append([int(x) for x in line.split()])

my_f.close()

print(sum(array[0]))