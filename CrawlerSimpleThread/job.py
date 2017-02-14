#!/usr/bin/python3

import queue


class Job(object):
    def __init__(self, priority, url):
        self.priority = priority
        self.url = url
        return

    def __lt__(self, other):
        return self.priority < other.priority

    def print_status(self, links: queue.PriorityQueue):
        print("Processed: " + self.url + " at depth " + str(self.priority) + ",", links.queue.__len__(),
              "items in queue")
