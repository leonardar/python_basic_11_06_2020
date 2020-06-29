# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать.
#
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
# прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json


if __name__ == '__main__':
    companies_proceeds = {}
    companies = 1
    counter = 0
    with open('file7.txt') as in_file:
        for line in in_file:
            name, ownership, income, expense = line.split()
            try:
                proceeds = int(income) - int(expense)
                if proceeds > 0:
                    companies *= proceeds
                    counter += 1
                companies_proceeds[name] = proceeds
            except ValueError:
                pass
    average = companies ** (1/counter)
    average_profit = {'average_profit': average}

    lst = []
    lst.append(companies_proceeds)
    lst.append(average_profit)

    with open('file7.1.json', 'w', encoding='UTF-8') as out_file:
        json.dump(lst, out_file, ensure_ascii=False)
