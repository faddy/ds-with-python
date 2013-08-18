#!/usr/sbin/python
"""
A small script to demo how the Locks are used
"""

import threading
import time

to_be_synced = []

class MyThread(threading.Thread):
    def __init__(self, thread_name):
        # instantiates the super class (Thread class)
        threading.Thread.__init__(self)
        self.thread_name = thread_name

    def run(self):
        # acquire threadLock
        threadLock.acquire()
        time.sleep(5)
        to_be_synced.append(self.thread_name)

        # release threadLock
        threadLock.release()
        print "done with thread " + self.thread_name


# get an instant of Lock
threadLock = threading.Lock()
threads = []

# create three threads
thread1 = MyThread("Thor")
thread2 = MyThread("IronMan")
thread3 = MyThread("CaptainAmerica")

# start all three threads
thread1.start()
thread2.start()
thread3.start()

# append the threads to a list of threads
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

# wait for all threads to finish
for t in threads:
    t.join()

print "exiting main thread!"
print "to_be_synced: " 
print to_be_synced
