#!/usr/bin/python

import threading
import Queue
import time

def process_data(thread_name, q):
    while not exit_signal:
        # acquire queue_lock
        queue_lock.acquire()
        
        # if queue is not empty, read data from queue
        if not q.empty():
            data = q.get()
            queue_lock.release()
            print thread_name, data
        else:
            queue_lock.release()
        time.sleep(1)


class MyThread(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.thread_name = name
        self.q = q

    def run(self):
        print "Starting thread " + self.thread_name
        process_data(self.thread_name, self.q)
        print "Finishing thread " + self.thread_name



print 'Starting main thread...'

name_list = ['Thor', 'CaptainAmerica', 'Hulk', 'IronMan', 'Black Widow', 'Arrow']
thread_list = []
exit_signal = False

# create queue_lock
queue_lock = threading.Lock()

# create queue
work_queue = Queue.Queue(10)

# start three threads
for name in ['One', 'Two', 'Three']:
    thread = MyThread(name, work_queue)
    thread.start()
    thread_list.append(thread)

# acquire lock on queue
queue_lock.acquire()

# populate the queue
for item in name_list:
    work_queue.put(item)

# release the lock
queue_lock.release()


# wait for queue to be empty
while not work_queue.empty():
    pass

# signal 'exit' to threads
exit_signal = True

# wait for threads to finish
for t in thread_list:
    t.join()

# die
print 'Finishing main thread'

