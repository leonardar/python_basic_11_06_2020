# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

from calendar import isleap


class Date:

    def __init__(self, date: str):
        if self.validate(date):
            self._day, self._month, self._year = self.parse(date)
        else:
            raise ValueError('Неверный формат')

    def __str__(self):
        return f'{self._day}-{self._month}-{self._year}'

    @classmethod
    def parse(cls, date: str):
        return tuple(map(int, date.split('-')))

    @staticmethod
    def validate(date: str) -> bool:
        thirty = [1, 3, 5, 7, 8, 10, 12]
        thirty_one = [4, 6, 9, 11]
        try:
            day, month, year = map(int, date.split('-'))
        except ValueError:
            return False
        if len(str(year)) == 4:
            if month == 2:
                if isleap(year) and 0 < day <= 29:
                    return True
                elif not isleap(year) and 0 < day <= 28:
                    return True
            elif month in thirty and 0 < day <= 30:
                return True
            elif month in thirty_one and 0 < day <= 31:
                return True
        return False


if __name__ == '__main__':
    date1 = Date('12-11-5678')
    print(date1)

    assert Date.validate('77-77-7777') == False
    assert Date.validate('11-11-1111') == True

    assert Date.parse('12-11-2001') == (12, 11, 2001)
