# Задание 5

from functools import reduce
my_list = [el for el in range(100, 1001, 2)]
# base list with even numbers

def my_func (prev_el, el):
    return prev_el * el

print(reduce(my_func, my_list))

