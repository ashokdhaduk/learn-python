#!/usr/bin/python3

import threading
import requests
import linkparser

from job import Job


class Worker(threading.Thread):
    def __init__(self, job: Job):
        super().__init__(name=job.url)

        self._job = job

    def run(self):
        self._job.print_status(linkparser.links)

        r = requests.get(self._job.url)

        link_parser = linkparser.LinkParser(self._job)

        link_parser.parse(r.text)

        linkparser.links = link_parser.get_links()
