import os
from collections import Counter
from typing import List


def data_handling(filename) -> List:
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def get_words_dict(words: List) -> dict:
    """Подсчет количества слов"""
    df_dict = Counter(words)
    sum_words = sum(df_dict.values())  # всего
    print(f"Кол-во слов: {sum_words}")

    set_words = list(df_dict)  # уникальных
    print(f"Кол-во уникальных слов: {len(set_words)}")

    sum_repeats = sum(filter(lambda x: x > 1, df_dict.values()))  # повторяемых
    print(f"Кол-во повторяемых слов: {sum_repeats}")

    return df_dict


def main():
    filename = input("Введите путь к файлу: ")
    if not os.path.exists(filename):
        print("Указанный файл не существует")
    else:
        words = data_handling(filename)
        words_dict = get_words_dict(words)

        print()
        print("Все использованные слова:")
        print("{:<20} {:<15}".format('Name', 'Value'))
        for name, n_comm in words_dict.items():
            print('{:<20} {:<15}'.format(name, n_comm))


if __name__ == '__main__':
    main()
