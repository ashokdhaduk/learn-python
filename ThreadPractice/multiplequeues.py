#!/usr/bin/python3

import queue
import threading
from urllib.request import urlopen
import time

hosts = ["http://caspaonline.com.au", "http://google.com", "http://lastdoorsolutions.com.au",
         "http://longwalkadventures.com", "http://bikemartnepal.com"]

q = queue.Queue()
output = queue.Queue()


class ThreadUrl(threading.Thread):
    def __init__(self, queue, out_queue):
        super().__init__()
        self.queue = q
        self.output = out_queue

    def run(self):
        host = self.queue.get()

        url = urlopen(host)
        chunk = url.read()

        self.output.put(host)

        self.queue.task_done()


class ParseUrl(threading.Thread):
    def __init__(self, out_queue):
        super().__init__()
        self.output = out_queue

    def run(self):
        chunk = self.output.get()

        print(chunk)

        self.output.task_done()


start = time.time()


def main():
    for i in range(6):
        t = ThreadUrl(q, output)
        t.setDaemon(True)
        t.start()

    for host in hosts:
        q.put(host)

    for i in range(6):
        t = ParseUrl(output)
        t.setDaemon(True)
        t.start()

    q.put('http://newmamastore.com')
    q.join()
    output.join()


main()
print("Time elapsed:", time.time() - start)
