#!/usr/bin/python3

from urllib.request import urlopen
import time
import threading
import queue

q = queue.Queue()

hosts = ["http://caspaonline.com.au", "http://google.com", "http://lastdoorsolutions.com.au",
         "http://longwalkadventures.com", "http://bikemartnepal.com"]

start = time.time()


class ThreadUrl(threading.Thread):
    """Threading url"""

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        h = self.queue.get()

        url = urlopen(h)
        print(url.read(512))
        print("Processed", h)

        self.queue.task_done()


def main():
    for i in range(5):
        t = ThreadUrl(q)
        t.setDaemon(True)
        t.start()


for host in hosts:
    q.put(host)

main()

q.join()
print("Elapsed time: ", time.time() - start)
