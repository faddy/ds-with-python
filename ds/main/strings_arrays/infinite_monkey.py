import random
import sys

alphabets = 'abcdefghijklmnopqrstuvwxyz '
target = 'methinks it is like a weasel'

def generate():
    s = ''
    for i in range(len(target)):
        random_i = random.randint(0, len(alphabets)-1)
        random_c = alphabets[random_i]
        s += random_c

    return s


def compare(s):
    diff = 0
    for i in range(len(s)):
        if s[i] != target[i]:
            diff += 1

    return diff


def main():
    count = 0
    min_diff = sys.maxint
    best_string = ''

    while True:
        count += 1
        random_s = generate()
        diff = compare(random_s)

        if diff < min_diff: 
            min_diff = diff
            best_string = random_s

        if diff == 0:
            print 'found it at try number {0}!'.format(count)
            print random_s, diff
            break
            
        if count%1000 == 0:
            print 'count:', count
            print 'min diff so far   :', min_diff
            print 'best string so far:', best_string
            print '---------------'
            
            
            
