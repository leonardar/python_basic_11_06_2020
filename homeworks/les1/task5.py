# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше
# издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.




while True:
    income = input('Введите доходы вашей фирмы за текущий период: ')
    if income.isdigit():
        income = int(income)
        break
    else:
        print('')

while True:
    expense = input('Введите расходы вашей фирмы за текущий период:  ')
    if expense.isdigit():
        expense = int(expense)
        break
    else:
        print('Это не число!')

proceeds = income - expense

if not proceeds <= 0:
        print('Бизнес прибыльный работаем дальше!')
        while True:
            rent = proceeds / income * 100
            emp = input('Введите численность сотрудников вашей фирмы: ')
            if emp.isdigit():
                emp = int(emp)
                break
            else:
                print('Это не число!')
        emp_inc = rent / emp
        print(emp_inc)
else:
    print('Бизнес не приносит прибыли!')


#
# while True:
#     emp = input('Введите численность сотрудников вашей фирмы: ')
#     if emp.isdigit():
#         emp = int(emp)
#         break
#     else:
#         print('Это не число!')




