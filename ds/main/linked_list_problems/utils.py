from data_structures.linked_lists import Node
import random


def create_linked_list(n):
    head = Node(1)
    p = head
    for i in range(n-1):
        p.nxt = Node( random.choice(range(5,9)) )
        p = p.nxt

    return head


def create_unique_linked_list(n):
    used_items = range(n)
    item = used_items.pop( random.choice(range(n)) )
    head = Node(item)
    p = head

    for i in range(n-1):
        item = used_items.pop( random.randrange(len(used_items)) )
        p.nxt = Node(item)
        p = p.nxt

    return head

def print_list(head):
    p = head
    while p:
        print p.data,
        p = p.nxt

    print

