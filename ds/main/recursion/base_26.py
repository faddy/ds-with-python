#!/usr/bin/python
'''
get_column_name() returns base 26 string for a given number.
eg. for n = 2, return value = 'b'
n = 23, val = 'w'
n = 30, val = 'ad'
n = 706, val = 'aad'
'''

def ret_char(i):
    if i < 0 or i > 26:
        raise Exception('invalid int value: {0}'.format(i))
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    return alphabets[i]


def get_col_name(n):
    s = ''
    while n > 0:
        rem = n % 26
        s = ret_char(rem) + s
        n = n/26

    return s
