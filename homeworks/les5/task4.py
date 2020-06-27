# 4. Создать (не программно) текстовый файл со следующим содержимым:

# One — 1
#
# Two — 2
#
# Three — 3
#
# Four — 4

# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

dct = {'One': 'Один',
       'Two': 'Два',
       'Three': 'Три',
       'Four': 'Четыре',}

if __name__ == '__main__':
    with open('file4.txt') as in_file:
        with open('file4.1.txt', 'w') as out_file:
            for line in in_file:
                try:
                    name, dash, number = line.split()
                    if name in dct.keys():
                        name = dct[name]
                    out_file.write(f'{name} {dash} {number}\n')
                except ValueError:
                    pass
