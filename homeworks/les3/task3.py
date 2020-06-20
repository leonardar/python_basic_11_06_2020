# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.


def my_func(x, y, z):
    if x >= z <= y:
        res = x + y
    elif y >= x <= z:
        res = y + z
    elif x >= y <= z:
        res = x + z
    return res


while True:
    x = input('Введите первое число:')
    if x.isdigit():
        x = int(x)
        break
    else:
        print('Попробуйте еще раз!')

while True:
    y = input('Введите второе число:')
    if y.isdigit():
        y = int(y)
        break
    else:
        print('Попробуйте еще раз!')

while True:
    z = input('Введите третье число:')
    if z.isdigit():
        z = int(z)
        break
    else:
        print('Попробуйте еще раз!')

print(my_func(x, y, z))
