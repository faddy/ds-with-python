#!/usr/bin/python

"""
A simple script to demo the threading module:
Create a Queue
Start 10 threads to process items in the Queue
Put items in the queue
Wait for all threads to finish
"""

import Queue
import threading
import time


def do_work(s, i):
    time.sleep(i)
    print '----', s, len(s)


def worker(i):
    while True:
        # get item from queue and do stuff with it
        item = q.get()
        do_work(item, i)
        # mark the item done in the queue
        q.task_done()

q = Queue.Queue()

# create 10 threads and start them
for i in xrange(10):
    t = threading.Thread(target=worker, args=(i,))
    t.daemon = True
    t.start()

# items to be put on the queue
for item in ['batman', 'superman', 'spiderman', 'hulk', 'wolverine', 'iron man', 'widow']:
    q.put(item)

# the main thread will wait for all the threads to finish
print 'main thread waiting for join..'
q.join()
