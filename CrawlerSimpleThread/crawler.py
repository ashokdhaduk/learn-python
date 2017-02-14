#!/usr/bin/python3

import requests
import linkparser

from job import Job
from worker import Worker


class Crawler:
    _depth = 3

    def crawl(self, job: Job):
        try:
            worker = Worker(job)
            worker.start()
            worker.join()
        except ValueError as e:
            print("Couldn't parse url: ", job.url, e)
            pass
        except (requests.ConnectionError, requests.ConnectTimeout, requests.exceptions.SSLError) as e:
            print("Couldn't parse url: ", job.url, e.strerror)
            pass
        else:
            while not linkparser.links.empty():
                job = linkparser.links.get()

                if job.priority < self._depth:
                    self.crawl(job)

            linkparser.links.task_done()

    def set_depth(self, depth: int):
        self._depth = depth


crawler = Crawler()
