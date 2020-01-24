# Задание 4


base_list = [2, 2, 5, 2, 7, 23, 1, 8, 44, 44, 3, 2, 23, 10, 7, 4, 11]
new_list = [el for el in base_list if base_list.count(el) == 1]
print(base_list)
print(new_list)