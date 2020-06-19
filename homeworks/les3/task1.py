# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.


def division(num1, num2):
    if num2 == 0:
        print('На ноль делить нельзя')
        return
    div = num1 / num2
    return div


while True:
    num1 = input('Введите первое число:')
    if num1.isdigit():
        num1 = int(num1)
        break
    else:
        print('Попробуйте еще раз!')

while True:
    num2 = input('Введите второе число:')
    if num2.isdigit():
        num2 = int(num2)
        break
    else:
        print('Попробуйте еще раз!')

res = division(num1, num2)
if res:
    print(res)
