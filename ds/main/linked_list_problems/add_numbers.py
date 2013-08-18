from data_structures.linked_lists import Node
from linked_list_problems.utils import print_list


def add_num(a, b, carry):
    s = a + b + carry
    return s % 10, 1 if s > 9 else 0

def add_two_lists(l1, l2):
    if not l1: return l2
    if not l2: return l1

    p1 = l1
    p2 = l2
    result = None
    p = None

    carry = 0
    while p1 and p2:
        s, carry = add_num(p1.data, p2.data, carry)

        if not result:
            result = Node(s)
            p = result

        else:
            p.nxt = Node(s)
            p = p.nxt

        p1 = p1.nxt
        p2 = p2.nxt

    t = p1 if p1 else p2

    while t:
        s, carry = add_num(t.data, 0, carry)
        p.nxt = Node(s)
        p = p.nxt
        t = t.nxt

    if carry:
        p.nxt = Node(1)

    return result


def make_list(num):
    if num is None: return

    n = num
    result = None
    p = None

    while n > 0:
        node = Node(n % 10)
        if not result:
            result = node
            p = result
        else:
            p.nxt = node
            p = p.nxt
        n = n / 10

    return result



if __name__ == '__main__':
    l1 = make_list(3123)
    print_list(l1)
    l2 = make_list(23956)
    print_list(l2)
    print_list(add_two_lists(l1, l2))
