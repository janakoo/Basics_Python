from functools import reduce
def proizvedenie(prev_el, el):
    return prev_el * el
list=[i for i in range(100,1001,2)]
print(reduce(proizvedenie, list))