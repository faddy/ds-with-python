from data_structures.stacks import Stack


def get_mod_value(num, base):
    # the base can be anything from 2 - 16
    # for any base < 10, return num.
    # for base > 10, mapping needs to happen to characters
    if base < 2 or base > 16: raise Exception('invalid base value')

    mapping = '0123456789abcdef'
    return mapping[num]


def base_convertor(decimal_num, base):
    if not isinstance(decimal_num, (int, long)): raise Exception('input must be a valid integer')

    if not isinstance(base, (int, long)) or base < 2 or base > 16: raise Exception('invalid base value')

    if decimal_num < 0: raise Exception('handling only positive numbers right now')

    st = Stack()
    while decimal_num != 0:
        rem = decimal_num % base
        st.push( get_mod_value(rem, base) )
        decimal_num /= base

    b = ''
    while not st.is_empty():
        b += st.pop()

    return b


def test():
    for i in [2, 3, 8, 10, 11, 16, 26]:
        print '%2d --> ' % i, base_convertor(26, i)

if __name__ == '__main__':
    test()
