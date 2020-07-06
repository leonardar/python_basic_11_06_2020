# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.

# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

# Примеры матриц вы найдете в методичке.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух
# матриц). Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.


class Matrix:

    __list_of_lists = []

    def __init__(self, list_of_lists):
        self.__list_of_lists = list_of_lists

    def __str__(self):
        result = ''
        for row in self.__list_of_lists:
            for item in row:
                result += f'{item:3} '
            result += '\n'
        return result

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError('Введенные данные не являются объектами одного класса')
        if len(other.__list_of_lists) != len(self.__list_of_lists):
            raise ValueError('Матрицы разного размера')

        result = []
        for i in range(len(other.__list_of_lists)):
            row = []
            for j in range(len(other.__list_of_lists[i])):
                row.append(self.__list_of_lists[i][j] + other.__list_of_lists[i][j])
            result.append(row)

        return Matrix(result)


if __name__ == '__main__':
    lst = [[i for i in range(10)] for i in range(5)]
    m = Matrix(lst)
    lst2 = [[i for i in range(10)] for i in range(5)]
    n = Matrix(lst2)
    print(m+n)
