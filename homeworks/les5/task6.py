# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.
#
# Примеры строк файла:
#
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
#
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


def extract_number(string):
    pos = 0
    for i, ch in enumerate(string):
        if ch not in '0123456789':
            pos = i
            break
    try:
        return int(string[0:pos])
    except ValueError:
        return 0


if __name__ == '__main__':
    dct = {}
    with open('file6.txt') as in_file:
        for line in in_file:
            key, lessons = line.split(':')
            total = 0
            for lesson in lessons.split():
                total += extract_number(lesson)
            dct[key] = total

    print(dct)
