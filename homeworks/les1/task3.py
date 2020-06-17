# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

while True:
    n = input('Введите любое число:')
    if not n.isdigit():
        print('Это не число!')
    else:
        break

n = int(n)
count = n + (n * 10 + n) + (n * 100 + n * 10 + n)
print(count)
