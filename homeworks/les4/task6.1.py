# 6. Реализовать два небольших скрипта:

# а) итератор, генерирующий целые числа, начиная с указанного,

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не
# должен быть бесконечным. Необходимо предусмотреть условие его завершения.

# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором
# также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from sys import argv
from itertools import count


def my_count(start_value, stop_value=10):
    for el in count(start_value):
        if el >= stop_value:
            break
        else:
            yield el


if len(argv) == 2:
    _, start_value = argv
    lst = [i for i in my_count(int(start_value))]
    print(lst)
elif len(argv) == 3:
    _, start_value, stop_value = argv
    lst = [i for i in my_count(int(start_value), int(stop_value))]
    print(lst)
else:
    print('Использование: python3 task6.1.py <start_value> [<stop_value>]')
