# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

seasons = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']

while True:
    month = input('Введите номер месяца от 1 до 12:')
    if month.isdigit() and 1 <= int(month) <= 12:
        month = int(month) - 1
        break
    else:
        print('Попробуйте еще раз!')

print(seasons[month])
