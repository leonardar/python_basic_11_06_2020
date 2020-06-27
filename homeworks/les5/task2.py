# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

if __name__ == '__main__':
    with open("file2.txt") as in_file:
        line_counter = 0
        word_counters = []
        for line in in_file:
            line_counter += 1
            word_counter = 0
            for _ in line.split():
                word_counter += 1
            word_counters.append(word_counter)

    print(f'Всего: {line_counter} строк')
    for i, word_counter in enumerate(word_counters):
        print(f'{i+1} строка содержит {word_counter} сл.')
