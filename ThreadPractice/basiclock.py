#!/user/bin/python3

import threading
from queue import Queue
import time

print_lock = threading.Lock()

q = Queue();


def job(worker):
    time.sleep(0.5)

    with print_lock:
        print(threading.current_thread().name, worker)


def threader():
    while True:
        worker = q.get()
        job(worker)
        q.task_done()


for x in range(10):
    t = threading.Thread(target=threader)
    t.setDaemon(True)
    t.start()

start = time.time()

for worker in range(20):
    q.put(worker)

q.join()

print('Time:', time.time() - start)
