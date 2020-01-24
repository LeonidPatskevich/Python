# Задание 3
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("base_3.txt", "r") as f:
    # создание словаря на основе файла
    my_dict = {}
    for line in f:
        name, salary = line.split()
        my_dict[name] = float(salary.replace('\n', ''))
    print(my_dict)

limit = 20000
for key, value in my_dict.items():
    if value < limit:
        print(key)

print(f'Average is {sum(my_dict.values()) / len(my_dict):.2f}')