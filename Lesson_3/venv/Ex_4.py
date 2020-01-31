# Задание 4

x = float(input('Введите основание :'))
y = int(input('Введите отрицательную степень :'))
while x <= 0 or y >= 0:
    print('Некорректные данные!')
    x = float(input('Введите основание :'))
    y = int(input('Введите отрицательную степень :'))

def my_func(x, y):
    """
    Calculation of degree without operator **

    """
    z = 1
    for i in range(abs(y)):
        z = z / x
    return z

print(my_func(x, y))


