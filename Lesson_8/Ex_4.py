# Задание 4, 5

from abc import ABC, abstractmethod

class Warehouse:
    def __init__(self, name):
        self.name = name
        self.count = {}

    def add_item(self, model_n, qty):
        self.count[model_n] = qty

    def sub_item(self, model_n, qty):
        self.qty_t = self.count[model_n]
        self.count[model_n] = self.qty_t - qty

class OfficeTech:

    @abstractmethod
    def __init__(self, model):
        self. model = model

class Scan(OfficeTech):

    def __init__(self, model):
        super().__init__(self, model)
        self. model = model

class Printer(OfficeTech):

    def __init__(self, model, tech):
        super().__init__(self, model)
        self. model = model
        self.tech = tech

class Xser(OfficeTech):

    def __init__(self, model):
        super().__init__(self, model)
        self. model = model

x_1 = Xser('Canon XC-7')
p_1 - Printer('Samsung SRT-450', 'laser')


