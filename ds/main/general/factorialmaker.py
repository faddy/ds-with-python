import math


def is_integer(number):
    return isinstance(number, int)


class FactorialMaker:

    """ Iterator to spit out factorials"""

    def __init__(self, limit):
	if is_integer(limit):
	    self.limit = limit
	else:
	    raise ValueError

	self.start = 0


    def __iter__(self):
	return self


    def next(self):
	self.start += 1
	if self.start > self.limit:
	    raise StopIteration
	return math.factorial(self.start)



def gen_factorial_maker(limit):
    if not is_integer(limit):
	raise ValueError
    
    for index in range(1, limit+1):
	yield math.factorial(index)
