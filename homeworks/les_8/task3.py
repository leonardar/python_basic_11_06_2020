# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на
# экран.

# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе
# пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если
# введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.


class Validator(Exception):

    def __init__(self):
        self._lst = []

    def validate(self):
        while True:
            try:
                a = input('Введите число(или "stop" для завершения работы):')
                if a == 'stop':
                    # print(f'Ваш итоговый список: {self._lst}')
                    break
                else:
                    a = int(a)
                    self._lst.append(a)
                    print(f'Ваш список на текущий момент: {self._lst}')
            except:
                print('Это не число! Повторите попытку ')
        return f'Ваш итоговый список: {self._lst}'


if __name__ == '__main__':
    try_except = Validator()
    print(try_except.validate())

