# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, re, im):
        self._re = re
        self._im = im

    def __add__(self, other):
        return ComplexNumber(self._re + other._re, self._im + other._im)

    def __sub__(self, other):
        return ComplexNumber(self._re - other._re, self._im - other._im)

    def __mul__(self, other):
        re = self._re * other._re - self._im * other._im
        im = self._im * other._re + self._re * other._im
        return ComplexNumber(re, im)

    def __str__(self):
        if self._im > 0:
            return f'{self._re} + i{self._im}'
        else:
            return f'{self._re} - i{abs(self._im)}'


if __name__ == '__main__':
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(-1, 3)

    print(c1)
    print(c2)

    print(c1 + c2)
    print(c1 - c2)
    print(c1 * c2)
