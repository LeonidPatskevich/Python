# Задание 1

class Matrix:
    def __init__(self, args):
        self.args = args

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.args]))

    def __add__(self, other):
        result = []
        num = []
        try:
            for i in range(len(self.args)):
                for j in range(len(self.args[i])):
                    if len(self.args[i]) == len(other.args[i]):
                        num.append(self.args[i][j] + other.args[i][j])
                        if len(num) == len(self.args[i]):
                            result.append(num)
                            num = []
                        else:
                            return "Матрицы не одинаковой размерности"
        except IndexError:
            print('Матрицы должны быть одинаковой размерности')
        return result

m_1 = Matrix([[6, 7], [4, 2], [8, 3]])
m_2 = Matrix([[6, 4], [6, 1], [2, 5]])
print(m_1)
print(m_1 + m_2)
