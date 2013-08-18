# convert a string to a number
# argument string can be:
# '123', '-32', '1', '0', '000', '-0'


class CustomException(Exception):
    def __init__(self):
        super(CustomException, self).__init__(self, 'Invalid characters in input')


def sanity_check(c):
    if ord(c) < ord('0') or ord(c) > ord('9'):
        return False
    else:
        return True


def get_int(c):
    print ord(c)
    return ord(c) - ord('0')


def atoi(s):
    if not s: raise CustomException()

    # if first char is '-'
    if s[0] == '-':
        neg = True
        s = s[1:]
        if not len(s): raise CustomException()
    else:
        neg = False

    final = 0
    for c in s:
        if not sanity_check(c): raise CustomException()
        else:
            final = get_int(c) + final*10

    return final if not neg else -final


def test():
    print atoi('555')
