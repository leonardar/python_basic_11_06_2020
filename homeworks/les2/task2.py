# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и
# 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

lst = input('Введите список элементов:').split()
# lst = [1, 2, 3, 5, 6, 7]

for i in range(1, len(lst), 2):
    lst[i], lst[i-1] = lst[i-1], lst[i]

print(lst)
