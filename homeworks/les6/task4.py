# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

TURN_RIGHT = 'направо'
TURN_LEFT = 'налево'


class Car:

    def __init__(self, car_color, car_name, is_police):
        self.car_speed = 0
        self.car_color = car_color
        self.car_name = car_name
        self.is_police = is_police

    def go(self, car_speed):
        self.car_speed = car_speed
        print(f'Машина поехала со скоростью {self.car_speed} км/ч')

    def stop(self):
        self.car_speed = 0
        print('Машина остановилась')

    def turn(self, direction):
        if direction == TURN_RIGHT:
            print('Машина повернула направо')
        elif direction == TURN_LEFT:
            print('Машина повернула налево')

    def show_speed(self):
        print(f'Текущая скорость автомобиля равна {self.car_speed} км/ч')


class TownCar(Car):

    def __init__(self, car_color, car_name):
        self.__town_car_max_speed = 60
        super().__init__(car_color, car_name, False)

    def show_speed(self):
        super().show_speed()
        if self.car_speed > self.__town_car_max_speed:
            print('Вы превысили скорость')


class SportCar(Car):

    def __init__(self, car_color, car_name):
        super().__init__(car_color, car_name, False)


class WorkCar(Car):

    def __init__(self, car_color, car_name):
        self.__work_car_max_speed = 40
        super().__init__(car_color, car_name, False)

    def show_speed(self):
        super().show_speed()
        if self.car_speed > self.__work_car_max_speed:
            print('Вы превысили скорость')


class PoliceCar(Car):

    def __init__(self, car_color, car_name):
        super().__init__(car_color, car_name, True)


if __name__ == '__main__':
    police_car1 = PoliceCar('Красный', 'Лада')
    print(police_car1.car_color)
    print(police_car1.car_name)
    police_car1.go(90)
    police_car1.show_speed()
    police_car1.turn(TURN_LEFT)
    police_car1.stop()

    work_car1 = WorkCar('Синий', 'Мерседес')
    print(police_car1.car_color)
    print(police_car1.car_name)
    police_car1.go(70)
    police_car1.show_speed()
    police_car1.turn(TURN_RIGHT)
    police_car1.stop()

    sport_car1 = SportCar('Пурпурный', 'BMW')
    print(police_car1.car_color)
    print(police_car1.car_name)
    police_car1.go(120)
    police_car1.show_speed()
    police_car1.turn(TURN_LEFT)
    police_car1.stop()

    town_car1 = TownCar('Бирюзовый', 'Форд')
    print(police_car1.car_color)
    print(police_car1.car_name)
    police_car1.go(60)
    police_car1.show_speed()
    police_car1.turn(TURN_RIGHT)
    police_car1.stop()
