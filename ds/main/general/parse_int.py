
# '724' --> 724

mapping = {k:v for k,v in zip('0123456789', range(10))}

def parse_int(s):
    if not s: return None

    if s[0] == '-':
        neg = True
        s = s[1:]
    else:
        neg = False

    val = 0
    radix = 0

    for i in xrange(len(s)-1, -1, -1):
        val += mapping[s[i]] * (10**radix)
        radix += 1

    return val if not neg else -val


if __name__ == '__main__':
    print parse_int('1')
    print parse_int('-1')
    print parse_int('312')
    print parse_int('0')
    print parse_int('-12344566845762341')
