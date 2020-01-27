# Задание 3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

val_1, val_2, val_3 = 4, 6, 8

def fun_max_sum (val_1, val_2, val_3):
    """
    Sum two of max

    """
    my_list = [val_1, val_2, val_3]
    sum_max = sum(my_list) - min(my_list)
    return sum_max

print(fun_max_sum (val_1, val_2, val_3))

