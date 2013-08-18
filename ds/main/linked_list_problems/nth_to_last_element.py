#!/usr/bin/python
from node_class import Node
from utils import create_linked_list, print_list


def nth_to_last_element(head, n):
    if not head: return None
    if n <= 0 : return None

    endp = head
    for i in range(n):
        if not endp: return None
        else: endp = endp.nxt

    p = head
    while(endp):
        p = p.nxt
        endp = endp.nxt

    return p


if __name__ == '__main__':
    head = create_linked_list(8)
    print_list(head)

    node = nth_to_last_element(head, 9)
    print node.data
