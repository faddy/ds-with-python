from data_structures.stacks import Stack


def reverse_using_stack(s):
    if not s: return s

    stack = Stack()
    for c in s:
        stack.push(c)

    new_s = ''
    while not stack.is_empty():
        new_s += stack.pop()

    return new_s


def reverse_using_swapping(s):
    if not s: return s

    arr = list(s)
    for i in range(len(arr)/2):
        beg = i
        end = len(arr)-1-i

        swap(arr, beg, end)

    return ''.join(arr)


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def test():
    print reverse_using_swapping('')
    print reverse_using_swapping('abcdef')
    print reverse_using_swapping('!@#$%^&*()')


if __name__ == '__main__':
    test()
