#!/usr/bin/python
import math
import random

def is_prime(n):
    n = abs(n)
    if n <= 2: return False 
    # check divisibility by items upto sqrt(n)
    for i in range(2, int(math.sqrt(n))+1, 1 ):
        if (n%i) == 0: return False

    return True


def hypotenuese(a, b):
    return math.sqrt(a**2 + b**2)


def int_with_probability(list_of_values):
    """Given a list of int values i, j, k...
       returns i with probability i, j with probability j, ...
    """
    sum_of_values = sum(list_of_values)
    # pick a random value from 0 to sum
    r = random.randrange(0, sum_of_values)
    new_sum = 0
    for item in list_of_values:
        new_sum += item
        if new_sum >= r:
            return item

#print is_prime(-13)
#print hypotenuese(3,4)

inp = [2,5,3,7,9,1,6]
inp = sorted(inp)
print sum(inp)

count = {}
for i in range(5000):
    v = int_with_probability(inp)
    count[v] = count.get(v, 0) + 1

print count

prob = {}
for item in count:
    prob[item] = (count[item]/5000.0, item/float(sum(inp)))

print prob

