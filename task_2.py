"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на практике
работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name: str):
        self.name = name

    @property
    @abstractmethod
    def calculator(self):
        pass


class Suit(Clothes):

    def __init__(self, name: str, h: float):
        super().__init__(name)
        self.h = h

    @property
    def calculator(self):
        return 2 * self.h + 0.3


class Coat(Clothes):

    def __init__(self, name: str, v: float):
        super().__init__(name)
        self.v = v

    @property
    def calculator(self):
        return self.v / 6.5 + 0.5


coat = Coat('Пальто', 3.5)
print(f'Пальто {round(coat.calculator, 2)}')

suit = Suit('Костюм', 1.9)
print(f'Костюм {round(suit.calculator, 2)}')

