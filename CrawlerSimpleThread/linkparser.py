#!/usr/bin/python3

import queue
import re

from job import Job
from html.parser import HTMLParser

links = queue.PriorityQueue()


class LinkParser(HTMLParser):
    _visited = []

    def __init__(self, job: Job):
        self._job = job
        super().__init__()

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            attrs = dict(attrs)

            if 'href' in attrs:
                if LinkParser.validate_url(attrs['href']):
                    if attrs['href'] not in links.queue and attrs['href'] not in self._visited:
                        links.put(Job(self._job.priority + 1, attrs['href']))

                    self._visited.append(attrs['href'])

    def parse(self, data):
        self.feed(data)

    def get_links(self):
        return links

    def print_links(self):
        for job in links.queue:
            print(job.description, job.priority)

    @staticmethod
    def validate_url(url: str):
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        return regex.match(url)
