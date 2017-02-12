#!/usr/local/bin/python3

from tagparser import tag_parser
import requests


def main():
    url = input("Enter web page url: ")

    try:
        r = requests.get(url)

        tag_parser.parse(r.text)

        tag_parser.print_analysis()
    except ValueError as e:
        print(e)
    except requests.exceptions.ConnectionError as e:
        print("Connection error: ", e.strerror)


if __name__ == '__main__':
    main()
else:
    print("Run from command line.")
