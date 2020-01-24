# Задание 4
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num_start = int(input('Введите целое положительное число: '))
num_res = 0
num = num_start
while num > 0:
    num_count = num % 10
    if num_count > num_res:
        num_res = num_count
    num = num // 10
print(f'Наибольшая цифра: {num_res}')