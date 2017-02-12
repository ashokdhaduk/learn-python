#!/usr/bin/python3

import codecs
from operator import itemgetter


def main():
    path = input("Enter file path: ")

    try:
        file = codecs.open(path, 'r+', encoding='utf8')

        word_list = map(lambda line: line.split(" "), file.readlines())

        print_words(count_words(word_list))

        file.close()
    except IOError as e:
        print(e.strerror, e.filename)
    except UnicodeDecodeError:
        print("Please enter a valid text file.")

    return


def count_words(word_list: list) -> tuple:
    words = dict()
    ignore = " ,.\n\r\t(){}[]-=+-\"\':#%*"

    for lines in word_list:
        for word in lines:
            if word in words:
                words[word.strip(ignore)] = words[word] + 1
            else:
                words[word.strip(ignore)] = 1

    return sorted(words.items(), key=itemgetter(1), reverse=True)


def print_words(words: tuple):
    """Print given words"""
    for word, count in words:
        print(word + ":", count)


if __name__ == "__main__":
    main()
else:
    print("Run from command line.")
