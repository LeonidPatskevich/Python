# Задание 4
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина едет')

    def stop(self):
        print('Машина стоит')

    def turn(self):
        print('Машина повернула')

    def show_speed(self):
        print(f"Скорость машины {self.speed} км/ч")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f"Машина превысила допустимую скорость")
        else:
            print(f"Скорость машины {self.speed} км/ч")


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f"Машина превысила допустимую скорость")
        else:
            print(f"Скорость машины {self.speed} км/ч")


class SportCar(Car):
 class PoliceCar(Car):

  town = TownCar(70, 'red', 'Mazda', False)
  town.show_speed()

  work = WorkCar(30, 'grey', 'Mersedes', False)
  work.show_speed()