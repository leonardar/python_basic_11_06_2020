# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.


def salary(hour, rate, award):
    return (hour * rate) + award


while True:
     hour = input('Введите количество выработанных часов:')
     if hour.isdigit():
         hour = int(hour)
         break
     else:
         print('Попробуйте еще раз!')


while True:
     rate = input('Введите вашу часовую тарифную ставку::')
     if rate.isdigit():
         rate = int(rate)
         break
     else:
         print('Попробуйте еще раз!')


while True:
     award = input('Введите вашу месячную премию:')
     if award.isdigit():
         award = int(award)
         break
     else:
         print('Попробуйте еще раз!')

print('Итого:', salary(hour, rate, award), 'рублей')
