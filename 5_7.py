import json
from statistics import mean

with open("E:/Python work/1/text_7.txt", 'r', encoding='utf-8') as file_inp:

    dohod_polozh, dohod, firma = [], [], []
    for line in file_inp:
        name, form, vyr, izder = line.split(' ')
        firma.append(name)
        dhd = float(vyr) - float(izder)
        dohod.append(dhd)
        if (dhd > 0):
            dohod_polozh.append(dhd)

    print(mean(dohod_polozh))
    print(sum(dohod_polozh) / len(dohod_polozh))
    print(dohod_polozh)

    my_dict = dict(zip(firma, dohod))
    m_list = [my_dict,{"average_profit": mean(dohod_polozh)} ]
    #my_dict.update({"average_profit": mean(dohod_polozh)})
    print(m_list)

    with open("task_7.json", "w") as write_f:
        json.dump(my_dict, write_f)