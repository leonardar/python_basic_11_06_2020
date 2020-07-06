# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2
# * H + 0.3). Проверить работу этих методов на реальных данных.

# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod
from typing import List


class Clothes(ABC):

    def __init__(self, name):
        self._clothes_name = name

    @abstractmethod
    def expense(self) -> float:
        pass


class Coat(Clothes):

    def __init__(self, V):
        super().__init__('coat')
        self._clothes_V = V

    def expense(self):
        return self._clothes_V / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, H):
        super().__init__('suit')
        self._clothes_H = H

    def expense(self):
        return 2 * self._clothes_H + 0.3


class ClothesStorage:
    __storage = []

    def __init__(self, other: List[Clothes]):
        self.__storage = other

    @property
    def storage(self):
        return self.__storage[:]

    @storage.setter
    def storage(self, other: List[Clothes]):
        self.__storage.update(other)

    def __getitem__(self, item: Clothes):
        return self.__storage[item]

    def total_expense(self):
        sum = 0
        for clothes in self.__storage:
            sum += clothes.expense()
        return sum


if __name__ == '__main__':
    s1 = Suit(5)
    print(s1.expense())
    c1 = Coat(13)
    print(c1.expense())

    storage = ClothesStorage([c1, s1])
    print(storage.total_expense())
