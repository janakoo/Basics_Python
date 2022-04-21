import re

file = open("text_6.txt","r")
values = file.read().split("\n")
data, name = [], []
for key in values:
    value = re.findall(r"[-+]?\d*\.\d+|\d+", key)
    value2 = re.findall(r"(?i)[a-z]+", key)
    if value != []:
        data.append([int(item) for item in value])
    if value2 != []:
        name.append(value2)
print(*[str(''.join(name[i])) + ' ' + str(sum(data[i])) + '\n' for i in range(len(data))])
file.close()