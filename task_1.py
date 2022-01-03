"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

   31	22         3	5	32         3	5	8	3
   37	43         2	4	6          8	3	7	1
   51	86         -1	64	-8

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, numbers: list):
        self.numbers = numbers

    def __add__(self, other: list):
        min_len = min([len(self.numbers), len(other.numbers)])
        if len(self.numbers) < len(other.numbers):  # реструктуризация матриц
            self.numbers, other.numbers = other.numbers, self.numbers

        for i in range(min_len):
            if len(self.numbers[i]) < len(other.numbers[i]):
                self.numbers[i], other.numbers[i] = other.numbers[i], self.numbers[i]

        new_list = self.numbers
        for i in range(min_len):
            for q in range(len(other.numbers[i])):
                self.numbers[i][q] += other.numbers[i][q]
        return Matrix(new_list)

    def __str__(self):
        return "\n".join(str(nums).strip('[]').replace(',', '') for nums in self.numbers)


print('Пример 1 сложение матрица 3х3')
a = Matrix([[35, 21, 25], [39, 10, 31], [40, 27, 10]])
print(f'Матрица a \n{a} \n')
b = Matrix([[32, 5, 20], [38, 10, 48], [35, 44, 43]])
print(f'Матрица b \n{b} \n')
c = a + b
print(f'Сумма матриц a и b \n{c} \n')

print('Пример 2 сложение 2 разных матриц')
d = Matrix([[15, 9, 24, 21], [25, 23, 35], [34, 36, 29, 42], [47, 36, 12]])
e = Matrix([[25, 15, 35], [17, 31, 21, 18], [40, 27, -3], [14, 30, 23, 24], [7, 37, -5]])
print(f'Матрица d \n{d}\n \nМатрица e \n{e} \n')


# def restructure_before_add(self, other: list):  # После данной функции остается сложить наименьшую общую часть
#     min_len = min([len(self.numbers), len(other.numbers)])  # также можно присвоить значения атрибутов временным
#     if len(self.numbers) < len(other.numbers):  # спискам чтобы исходные объекты остались неизменными
#         self.numbers, other.numbers = other.numbers, self.numbers
#
#     for i in range(min_len):
#         if len(self.numbers[i]) < len(other.numbers[i]):
#             self.numbers[i], other.numbers[i] = other.numbers[i], self.numbers[i]
#
#
# restructure_before_add(d, e)

print(f'{d}\n \n{e}\n')

f = d + e
print(f'Сумма матриц d и e \n{f} \n')
