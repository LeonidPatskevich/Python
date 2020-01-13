# Задание 3
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Реализация через dict.
month = int(input('Введите номер месяца: '))
while month < 0 or month > 12:
    month = int(input('Неверно, введите номер месяца: '))

seasons = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer',
           8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
print(seasons[month])

# Реализация через list.
month = int(input('Введите номер месяца: '))
while month < 0 or month > 12:
    month = int(input('Неверно, введите номер месяца: '))
seasons = ('winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn',
           'autumn', 'autumn', 'winter')
print(seasons[month - 1])