

def map_digit_to_string(n, base):

    table = {10: '0123456789',
             16: '0123456789abcdef',
              2: '01',
              8: '01234567'}

    return table[base][n]



def to_str(n, base):

    if base <= 1: raise Exception('invalid base')

    if n < base:
        return map_digit_to_string(n, base)

    # f(n/10) + value_of(n%10) --> recurse
    return to_str(n/base, base) + map_digit_to_string(n%base, base)
