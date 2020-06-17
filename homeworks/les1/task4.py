# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте
# цикл while и арифметические операции.
#



while True:
    n = input('Введите целое положительное число:')
    if n.isdigit() and int(n) > 0:
        n = int(n)
        break
    else:
        print('Это не целое положительное число!')


max_fig = 0


while n and max_fig != 9:
    fig = n % 10
    if fig > max_fig:
        max_fig = fig
    n //= 10

print(max_fig)