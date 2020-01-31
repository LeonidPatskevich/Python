# Задание 2
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

user_name = 'Alex'
user_surname = 'Ivanov'
user_year_b = 1985
user_town = 'Moscow'
user_mail = 'ivanov@mail.ru'
user_phone = 79163551819

def user_date (user_name, user_surname, user_year_b, user_town, user_mail, user_phone):
    print(user_name, user_surname, user_year_b, user_town, user_mail, user_phone)
    return

print('User info :')
user_date(user_name, user_surname, user_year_b, user_town, user_mail, user_phone)