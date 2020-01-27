# Задание 3
# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self, name, surname):
        print(name, '', surname)

    def get_total_income(self, _income):
        print(f"Total income : {_income['wage'] + _income['bonus']}")


emploer_1 = Position('Alex', 'Ponomarev', 'guardian', {'wage': 1600, 'bonus': 400})

print(emploer_1.name)
print(emploer_1.surname)
print(emploer_1.position)
print(emploer_1._income)

emploer_1.get_full_name(emploer_1.name, emploer_1.surname)
emploer_1.get_total_income(emploer_1._income)
