# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Office_equipment:

    _description = {}

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self._description = {}

    def __str__(self):
        return f'{self._description}'

    @classmethod
    def reception(cls):
        while True:
            try:
                name = input(f'Введите наименование: ')
                price = int(input(f'Введите стоимость за шт. : '))
                quantity = int(input(f'Введите общее количество: '))
                if name in cls._description.keys() and cls._description[name][0] == f'Стоимость: {price} рублей':
                    for elem in cls._description[name][1].split():
                        if elem.isdigit():
                            prm = int(elem) + quantity
                            cls._description[name][1] = f'Количество: {prm} шт.'
                else:
                    cls._description[name] = [f'Стоимость: {price} рублей']
                    cls._description[name].append(f'Количество: {quantity} шт.')
                print('В магазин отправлено: ', name, ', '.join(str(num) for num in cls._description[name]))
                q = input('Для выхода нажмите q или ENTER для продолжения ввода: ')
                if q == 'Q' or q == 'q':
                    break
            except ValueError:
                return f'Неверный формат'
        return cls._description

class Printer(Office_equipment):

    def __init__(self, model):
        self.model = model

    def operate(self, quantity):
        return f'Распечатано количество раз: {quantity}'


class Scanner(Office_equipment):

    def __init__(self, model):
        self.model = model

    def operate(self, quantity):
        return f'Отсканировано количество раз{quantity} times'


class Copier(Office_equipment):

    def __init__(self, model):
        self.model = model

    def operate(self, quantity):
        return f'Количество копий: {quantity}'


if __name__ == '__main__':

    cl1 = Office_equipment('hp', 2000, 5)
    printer1 = Printer(687)
    print(printer1.operate(7))

    print(cl1.reception())
