#!/usr/bin/python

def a_decorator(fn):
    def a_wrapper(*args, **kwargs):
        print 'hey! i am a wrapper!'
        print  'args: {0} \nkwargs: {1}'.format(args, kwargs)
        print '------------'
        fn(*args, **kwargs)

    return a_wrapper


def benchmark(fn):
    '''
    A decorator that prints the time a function takes
    to execute
    '''
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        for x in xrange(1000):
            res = fn(*args, **kwargs)
        print fn.__name__, (time.clock()-t)
        return res

    return wrapper


def logging(fn):
    '''
    A decorator that logs the activity of a function
    '''
    import logging
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        print fn.__name__, args, kwargs
        return res

    return wrapper


@logging
def print_full_name(food, description, hero, villian):
    print 'kind:' , food
    print 'description: ', description
    print 'hero:', hero
    print 'villian:', villian

#print_full_name(food='burger', description='this is lame', hero='batman', villian='joker')



### using functools.wraps
import functools

def bar(fn):
    @functools.wraps(fn)
    def wrapper():
        print 'bar'
        res = fn()
        return res

    return wrapper

@bar
def foo():
    print 'foo'


foo()

print 'foo name: ', foo.__name__

