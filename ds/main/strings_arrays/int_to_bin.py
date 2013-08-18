from data_structures.stacks import Stack


def dec_to_bin(n):
    if not isinstance(n, (int, long)): raise Exception('Not an int value')

    st = Stack()
    while n != 0:
        st.push(n % 2)
        n = n/2

    b = ''
    while not st.is_empty():
        b += str(st.pop())

    return b


def test():
    print dec_to_bin(5)
    print dec_to_bin(0)
    print dec_to_bin(8)
    print dec_to_bin(15)


if __name__ == '__main__':
    test()
