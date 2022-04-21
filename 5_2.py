m_f = open("m2_file.txt", 'r')
content = m_f.read()
print('Текст файла: \n', content)
m_f.close()

m_f = open("m2_file.txt", 'r')
count = sum(1 for line in m_f if line.rstrip('\n'))
print('Количество строк: ', count)
m_f.close()

m_f = open("m2_file.txt", 'r')
str = m_f.readlines()
for i in range(len(str)):
   print(f'Количество слов в строке {i+1}: {len(str[i].split())} шт')

m_f.close()