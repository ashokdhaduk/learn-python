#!/usr/bin/python3

import argparse

from crawler import crawler
from job import Job


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="Web page url to crawl")
    parser.add_argument("--depth", help="Crawl depth, defaults to 3")
    args = parser.parse_args()

    try:
        url = args.url or input("Enter web page url to crawl: ")

        crawler.set_depth(int(args.depth) or 3)
        crawler.crawl(Job(0, url))
    except KeyboardInterrupt as e:
        print("\nCrawling aborted by user")


if __name__ == '__main__':
    main()
else:
    print("Run from command line.")
