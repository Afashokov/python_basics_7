"""
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение (add()),
вычитание (sub()), умножение (mul()), деление (truediv()). Данные методы должны
применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между
\n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в
последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке
https://pythonworld.ru/osnovy/peregruzka-operatorov.html.
"""


class Cell:

    def __init__(self, units: int):
        if units > 0:
            self.units = units
        else:
            print('Количество ячеек должно быть больше 0')
            exit()

    def is_cell(self, other):
        if not isinstance(other, self.__class__):
            print('Операции допустимы только между объектами класса Cell')
            exit()

    def __add__(self, other: int):
        self.is_cell(other)
        tmp_units = self.units + other.units
        return Cell(tmp_units)

    def __sub__(self, other: int):
        self.is_cell(other)
        tmp_units = self.units - other.units
        if tmp_units > 0:
            return Cell(tmp_units)
        else:
            print('Разность ячеек должна быть больше 0')
            exit()

    def __mul__(self, other: int):
        self.is_cell(other)
        tmp_units = self.units * other.units
        return Cell(tmp_units)

    def __truediv__(self, other: int):
        self.is_cell(other)
        tmp_units = round(self.units / self.units)
        return Cell(tmp_units)

    def __str__(self):
        return str(self.units)

    @property
    def counter(self):
        return self.units

    def arrange(self: int, units_in_str: int):
        items = '*' * self.counter
        for i in range(0, len(items), units_in_str):
            print(items[i:i + units_in_str])


cell_1 = Cell(8)
cell_2 = Cell(6)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

Cell.arrange((cell_1 * cell_2), 7)

