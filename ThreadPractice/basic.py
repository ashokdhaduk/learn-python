#!/usr/bin/python3

import threading
import datetime


class MyThread(threading.Thread):
    def run(self):
        now = datetime.datetime.now()
        print(self.getName(), "says hello world at:", now)


for i in range(2):
    t = MyThread()
    t.start()
