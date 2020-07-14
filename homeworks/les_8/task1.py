# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.


class Date:

    def __init__(self, date: str):
        if self.validate(date):
            self.parse(date)
        else:
            raise ValueError('Неверный формат')

    def __str__(self):
        return f'{self._day}-{self._month}-{self._year}'

    @classmethod
    def parse(cls, date: str):
        cls._day, cls._month, cls._year = map(int, date.split('-'))

    @staticmethod
    def validate(date: str) -> bool:
        try:
            day, month, year = map(int, date.split('-'))
        except ValueError:
            return False
        if 0 < day <= 31 and 0 < month <= 12 and len(str(year)) == 4:
            return True
        else:
            return False


if __name__ == '__main__':
    date1 = Date('12-11-5678')
    print(date1)

    print(Date.validate('77-77-7777'))
    print(Date.validate('11-11-1111'))

    print(Date.parse('12-11-2001'))
