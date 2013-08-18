#!/usr/bin/ipython -i

import threading
import time


def target_thread(interval):
    print 'starting thread for interval: {0}'.format(interval)

    while True:
        print 'sleeping...'
        time.sleep(interval)



def main():
    print 'In main thread'
    interval = 5
    t = threading.Thread(target=target_thread, args=(interval,))
    t.daemon = True
    t.start()

    print 'waiting for target_thread to finish'
    t.join(4)

    print 'target thread is alive?', t.isAlive()

    return t

    
if __name__ == '__main__':
    thread = main()
