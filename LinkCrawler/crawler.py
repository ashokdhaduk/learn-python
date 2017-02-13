#!/usr/bin/python3

import requests
import queue

from job import Job
from linkparser import LinkParser


class Crawler:
    _depth = 3

    def crawl(self, job: Job):
        try:
            r = requests.get(job.url)

            link_parser = LinkParser(job)

            link_parser.parse(r.text)

            links = link_parser.get_links()
        except ValueError as e:
            print("Couldn't parse url: ", job.url, e)
            pass
        except (requests.ConnectionError, requests.ConnectTimeout) as e:
            print("Couldn't parse url: ", job.url, e.strerror)
            pass
        else:
            while not links.empty():
                job = links.get()

                self.print_status(job, links)

                if job.priority < self._depth:
                    self.crawl(job)

    def set_depth(self, depth: int):
        self._depth = depth

    @staticmethod
    def print_status(job: Job, links: queue.PriorityQueue):
        print("Processed: " + job.url + " at depth " + str(job.priority) + ",", links.queue.__len__(),
              "items in queue")


crawler = Crawler()
