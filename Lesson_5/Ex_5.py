# Задание 5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open("base_5.txt", "w+") as f:
    str_list = [randint(0, 100) for i in range(10)]
    f.writelines(' '.join(list(map(str, str_list))))
    f.seek(0, 0)
    print(sum(str_list))

