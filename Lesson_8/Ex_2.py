# Задание 2

class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    div_first = float(input('Введите делимое :'))
    div_sec = float(input('Введите делитель :'))

    if div_sec == 0:
        raise ZeroError("На ноль делить нельзя!")
except ValueError:
    print('Вы ввели не число!')
except ZeroError as txt:
    print(txt)
else:
    res = div_first / div_sec
    print(f"Все хорошо. {div_first} / {div_sec}​= {res}")




