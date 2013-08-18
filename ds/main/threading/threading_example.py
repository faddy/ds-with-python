#!/usr/bin/python
"""
Program to demo how to create and start threads
"""
from threading import Thread
import time

def print_time(thread_name):
    print "%s: %s" % (thread_name, time.ctime(time.time()))
    time.sleep(5)
    print "%s: %s" % (thread_name, time.ctime(time.time()))

class MyThread(Thread):
    """The MyThread class, whose instance will be run as a thread. 
    The run() method is where all the action takes place
    """
    def __init__(self, thread_name):
        Thread.__init__(self)
        self.thread_name = thread_name

    def run(self):
        print "Starting thread " + self.thread_name
        print_time(self.thread_name)
        print "Exiting " + self.thread_name


thread1 = MyThread("First")
thread2 = MyThread("Second")

print "Starting the threads"

thread1.start()
thread2.start()

print "Exiting main thread"
