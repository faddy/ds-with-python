from data_structures.linked_lists import Node
from linked_list_problems.utils import create_unique_linked_list, print_list
import random


def find_loop_start(head):
    if not head or not head.nxt: return None
    if head.nxt == head: return head

    p1 = p2 = head

    while True:
        p1 = p1.nxt
        p2 = p2.nxt.nxt

        if p1 == p2: break

    newp = head
    while newp != p1:
        newp = newp.nxt
        p1 = p1.nxt

    return newp
    

def add_loop(head, n):
    if not head: return
    if not head.nxt: return

    last = loop_start = head
    while last.nxt: last = last.nxt
    
    for i in range( random.randrange(5) ):
        loop_start = loop_start.nxt

    last.nxt = loop_start
    print loop_start.data


if __name__ == '__main__':
    n = 12
    head = create_unique_linked_list(n)
    print_list(head)
    add_loop(head, n)

    node = find_loop_start(head)
    print node.data
