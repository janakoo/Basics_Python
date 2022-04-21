f = open("E:/Python work/1/text_4.txt", 'r', encoding='utf-8')
dict = {'One': 'Один', 'Two': 'Два',  'Three': 'Три',  'Four': 'Четыре'}
my_list = [i.split() for i in f]
f.close()
for i in range (len(my_list)):
    my_list[i][0]=dict[list(dict)[i]]
f2 = open("E:/Python work/1/text_42.txt", 'w', encoding='utf-8')
for i in range(len(my_list)):
    print(' '.join(my_list[i]),file=f2)
f2.close()

f2 = open("E:/Python work/1/text_42.txt", 'r', encoding='utf-8')
f2_r = f2.read()
print(f2_r)
f2.close()