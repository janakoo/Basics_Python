mein_f = open("m_file.txt", "w")
while True:
    str_list = input("Введите текст:")
    mein_f.write(str_list+'\n')
   # print(str_list)

    if str_list == "":
        break
mein_f.close()

mein_f = open("m_file.txt", "r")
content = mein_f.read()
print("Записанный текст:\n", content)
mein_f.close()