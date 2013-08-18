import threading


class Reader(threading.Thread):
    def __init__(self, name, cache):
        threading.Thread.__init__(self)
        self.name = name
        self.cache = cache
        print 'Thread with name {0} has been initialized'.format(name)

    def run(self):
        print 'I am in the run method, bro'
        print self.get_value_from_cache()

    def get_value_from_cache(self):
        value = self.cache.get(self.name)
        return value

