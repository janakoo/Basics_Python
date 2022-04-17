from sys import argv

script_name, vyr, stav, prem = argv
print("Имя скрипта расчета зарплаты: ", script_name)
print("Выработка: ", vyr)
print("Ставка: ", stav)
print("Премия: ", prem)
print("Зарплата равна: ", float(vyr)*float(stav)+float(prem))