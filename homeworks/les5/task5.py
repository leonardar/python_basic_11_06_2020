# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

if __name__ == '__main__':
    with open('file5.txt', 'w') as out_file:
        for _ in range(10):
            out_file.write(f'{randint(0, 100)} ')

    sum = 0
    with open('file5.txt') as in_file:
        for el in in_file.readline().split():
            try:
                sum += int(el)
            except ValueError:
                pass
    print(f'Итого: {sum}')
