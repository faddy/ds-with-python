# sort a stack in ascending order using only these functions:
# push(), pop(), peek(), is_empty()

from data_structures.stacks import Stack


def sort_stack(orig):
    if not orig or not isinstance(orig, Stack):
        return None

    dup = Stack()

    while not orig.is_empty():
        item = orig.pop()

        if dup.is_empty():
            dup.push(item)

        elif item >= dup.peek():
            dup.push(item)

        else:
            while item < dup.peek():
                orig.push(dup.pop())

            orig.push(item)

            while not dup.is_empty():
                orig.push(dup.pop())


    while not dup.is_empty():
        orig.push(dup.pop())


def test():
    s = Stack()
    s.push(44)
    s.push(32)
    s.push(39)
    s.push(-22)
    s.push(14)

    print s.data

    sort_stack(s)

    print s.data


if __name__ == '__main__':
    test()
