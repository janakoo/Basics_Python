me_f = open("text_3.txt", 'r', encoding='utf-8')
salary = []

m_list = me_f.read().split("\n")

for i in m_list:
    i = i.split()

    if float(i[1]) < 20000:
        print(i[0])
    salary.append(float(i[1]))
print(sum(salary)/len(salary))

me_f.close()