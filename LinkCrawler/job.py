#!/usr/bin/python3


class Job(object):
    def __init__(self, priority, url):
        self.priority = priority
        self.url = url
        return

    def __lt__(self, other):
        return self.priority < other.priority
