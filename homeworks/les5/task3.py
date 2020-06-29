# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.

if __name__ == '__main__':
    with open('file3.txt') as in_file:
        average = 0
        lines = 0
        for line in in_file:
            try:
                name, salary = line.split()
                salary = int(salary)
                average += int(salary)
                if int(salary) < 20000:
                    print(f'С окладом менее 20 тыс.руб работает г-н {name}')
            except ValueError:
                pass
            lines += 1
        print(f'Средняя величина дохода сотрудников составляет {average/lines}')
