# Задание 4

dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("base_4.txt") as base_f:
    line = base_f.read().split("\n")
    for i in line:
        i = i.split(" - ")
with open("base_44.txt", "a") as new_f:
    new_f.writelines(dict[i[0]] + ' - ' + i[1] + "\n")
