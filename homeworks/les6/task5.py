# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.


class Stationery:

    def __init__(self, stationery_title):
        self.stationery_title = stationery_title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self, stationery_title):
        super().__init__(stationery_title)

    def draw(self):
        print(f'Инструмент нашего творческого урока: {self.stationery_title}')


class Pencil(Stationery):

    def __init__(self, stationery_title):
        super().__init__(stationery_title)

    def draw(self):
        print(f'Инструмент нашего творческого урока: {self.stationery_title}')


class Handle(Stationery):

    def __init__(self, stationery_title):
        super().__init__(stationery_title)

    def draw(self):
        print(f'Инструмент нашего творческого урока: {self.stationery_title}')


if __name__ == '__main__':
    pencil1 = Pencil('Карандаш')
    handle1 = Handle('Маркер')
    pen1 = Pen('Ручка')

    pencil1.draw()
    handle1.draw()
    pen1.draw()
