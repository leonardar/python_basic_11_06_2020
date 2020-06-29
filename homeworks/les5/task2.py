# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

if __name__ == '__main__':
    with open('file2.txt') as in_file:
        line_counter = 0
        word_counters = []
        for line in in_file:
            line_counter += 1
            word_counter = 0
            for _ in line.split():
                word_counter += 1
            word_counters.append(word_counter)

    print(f'Всего строк: {line_counter}')
    for i, word_counter in enumerate(word_counters):
        figure = word_counter % 10
        if figure == 1 and word_counter != 11:
            print(f'{i+1}-я строка содержит {word_counter} слово')
        elif 1 < figure < 5 and not 11 < word_counter < 15:
            print(f'{i+1}-я строка содержит {word_counter} слова')
        else:
            print(f'{i+1}-я строка содержит {word_counter} слов')
