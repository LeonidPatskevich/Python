# Задание 5
# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    title = 'название'

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        title = 'ручки'
        print(f"Запуск отрисовки {title}")


class Pencil(Stationery):

    def draw(self):
        title = 'карандашом'
        print(f"Отрисовка {title}")


class Handle(Stationery):

    def draw(self):
        title = 'маркером'
        print(f"Начало отрисовки {title}")


Pen_1 = Pen()
Pen_1.draw()
Pencil_1 = Pencil()
Pencil_1.draw()
Handle_1 = Handle()
Handle_1.draw()
