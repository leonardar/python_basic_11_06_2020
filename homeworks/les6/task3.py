# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position, income):
        self.worker_name = name
        self.worker_surname = surname
        self.worker_position = position
        self._worker_income = income


class Position(Worker):

    def get_full_name(self):
        return f'{self.worker_name} {self.worker_surname}'

    def get_total_income(self):
        return self._worker_income['wage'] + self._worker_income['bonus']


if __name__ == '__main__':
    pos1 = Position('Игорь', 'Петров', 'менеджер', {'wage': 20000, 'bonus': 5000})
    assert pos1.get_full_name() == 'Игорь Петров'
    assert pos1.get_total_income() == 25000
