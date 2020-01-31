# Задание 3

class Cell:
    # конструктор класса Cell
    def __init__(self, num_c):
        self.num_c = num_c

    # создаем свойство клетки

    @property
    def num_c(self):
        return self.__num_c

    # сеттер для создания свойств

    @num_c.setter
    def num_c(self, num_c):
        if type(num_c) is int and num_c > 0:
            self.__num_c = num_c
        else:
            self.__num_c = abs(round(num_c))

    def __add__(self, other):
        return Cell(self.num_c + other.num_c)

    def __sub__(self, other):
        if self.num_c <= other.num_c:
            print('Операция невозможна')
        else:
            return Cell(self.num_c - other.num_c)

    def __mul__(self, other):
        return Cell(self.num_c * other.num_c)

    def __truediv__(self, other):
        return Cell(self.num_c // other.num_c)

    def __str__(self):
        return f"Клетка с ячейками (​ {self.num_c}​ )"

    def make_order(self, snow_in_row): # зависает
        self.snowfall = ""
        while self.num_c > 0:
            self.num_c -= snow_in_row
            if self.num_c < 0:
                self.snowfall += ("*" * (snow_in_row + self.num_c) + "\n")
            else:
                self.snowfall += ("*" * snow_in_row + "\n")
        return self.snowfall

    def __call__(self, new_num_c):
        self.num_c = new_num_c



a = Cell(-10.37)
b = Cell(8)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(b.make_order(3))
