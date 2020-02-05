# Задание 3

class NumError(Exception):
    def __init__(self, txt):
        self.txt = txt


res_num = []
i = 0
while True:
    try:
        i = input('Введите число :')
        if i == "stop":
            break
        if i.isdigit() == False: # выпадает из цикла
            raise NumError('Вы ввели строку')
    except NumError as err:
        print(err)
    res_num.append(float(i))

print(res_num)
