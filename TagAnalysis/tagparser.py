#!/usr/local/bin/python3

from html.parser import HTMLParser


class TagParser(HTMLParser):
    analysis = []

    def error(self, message):
        print(message)

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)

        if tag == 'img':
            if 'alt' not in attributes or not attributes['alt']:
                position = self.getpos()
                self.analysis.append(
                    "<img>, line " + str(position[0]) + ", column " +
                    str(
                        position[1]) + ": alt attribute is missing or empty"
                    )

        elif tag == 'a':
            if 'href' not in attributes:
                position = self.getpos()
                self.analysis.append(
                    "<a>, line " + str(position[0]) + ", column " + str(position[1]) + ": href attribute is missing"
                )

    def parse(self, data):
        self.feed(data)

    def get_analysis(self):
        return self.analysis

    def print_analysis(self):
        for result in self.analysis:
            print(result)


tag_parser = TagParser()
