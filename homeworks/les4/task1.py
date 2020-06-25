# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary(hour, rate, award):
    return (hour * rate) + award


if len(argv) == 4:
    _, hours, rate, award = argv
    if hours.isdigit() and rate.isdigit() and award.isdigit():
        print('Итого:', salary(int(hours), int(rate), int(award)), 'рублей')
else:
    print('Использование: python3 task1.py <hours> <rate> <award>')
