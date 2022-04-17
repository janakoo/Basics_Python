from itertools import cycle
с = 0
for el in cycle([1,2,3,4]):
    if с > 10:
        break
    print(el)
    с += 1