# caching:

import threading
import reader
import Queue
import time

class AccountCache():
    def __init__(self):
        self.__cache = {}
        self.__lock = threading.Lock()
        self.__dirty = False
        self.__refresh_interval = 60

        self.refresh_thread = threading.Thread(target=self.refresh_cache)
        self.refresh_thread.daemon = True
        self.refresh_thread.start()

    def set(self, key, value):
        with self.__lock:
            self.__cache[key] = value
            self.__dirty = True

    def get(self, key):
        value = None

        with self.__lock:
            value = self.__cache.get(key, None)
            if not value:
                value = get_accounts_from_somewhere(key)    ## can also be replaced by pull for all accounts
                self.__cache[key] = value

        return value

    def has_key(self, key):
        is_exists = False
        with self.__lock:
            is_exists = self__cache.has_key(key)

        return is_exists

    def print_cache(self):
        with self.__lock:
            print self.__cache

    def refresh_cache(self):
        local_cache = get_accounts_from_somewhere()

        with self.__lock:
            self.__cache = local_cache
            self.__dirty = False

        time.sleep(self.__refresh_interval)



def get_accounts_from_somewhere(key=None):
    d = {}
    d['fahad'] = 'Fahad Ghani'
    d['anam'] = 'Anam Ghani'
    d['nash'] = 'Nasreen Ghani'
    d['ken'] = 'Ken Elkabany'

    if key:
        return d.get(key, None)
    else:
        return d


if __name__ == '__main__':
    cache = AccountCache()

    threads = []
    threads.append(reader.Reader('faddy', cache))
    threads.append(reader.Reader('ken', cache))

    for t in threads:
        t.start()

    print threading.active_count()
