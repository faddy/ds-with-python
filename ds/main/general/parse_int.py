
# '724' --> 724

mapping = {k:v for k,v in zip('0123456789', range(10))}

def parse_int(s):
    if not s: return None

    val = 0
    radix = 0
    for i in xrange(len(s)-1, -1, -1):
        val += mapping[s[i]] * (10**radix)
        radix += 1

    return val
