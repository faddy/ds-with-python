# sort a stack in ascending order using only these functions:
# push(), pop(), peek(), is_empty()

from stack_implementations import StackWithList


def sort_stack(orig):
    if not orig or not isinstance(orig, StackWithList):
        return None

    dup = StackWithList()

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
    s = StackWithList()
    s.push(44)
    s.push(32)
    s.push(39)
    s.push(-22)
    s.push(14)

    print s.storage

    sort_stack(s)

    print s.storage
