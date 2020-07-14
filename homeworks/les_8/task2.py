# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class ExceptNull(Exception):

    def __str__(self):
        return f'На ноль делить нельзя!'


def divide(dividend, denominator):
    if denominator == 0:
        raise ExceptNull
    return dividend / denominator


if __name__ == '__main__':

    while True:
        dividend = input("Введите делимое: ")
        denominator  = input("Введите делитель: ")
        try:
            a = int(dividend)
            b = int(denominator)
            c = divide(a, b)
            print(c)
        except ExceptNull as e:
            print(e)





