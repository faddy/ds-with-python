import random
import data_structures.linked_lists as ll

def remove_dups_using_dict(head):
    '''
    Removes duplicate nodes from a linked list
    '''
    if not head: return
    if not head.nxt: return	# only 1 node in the list

    items_seen = {head.data:True}
    ptr = head

    while ptr.nxt:
        val = items_seen.get(ptr.nxt.data, False)
        if not val:
            items_seen[ptr.nxt.data] = True
            ptr = ptr.nxt
        else:
            ptr.nxt = ptr.nxt.nxt


def construct_linked_list(num_nodes, upper_limit):
    if not num_nodes: return None
    head = ll.Node(random.randint(0, upper_limit))
    p = head

    for i in range(num_nodes-1):
        n = ll.Node(random.randint(0, upper_limit))
        p.nxt = n
        p = p.nxt

    return head


def print_list(head):
    if not head: return
    p = head

    while p:
        print str(p.data) + ' ',
        p = p.nxt

    print


if __name__ == '__main__':
    list_head = construct_linked_list(10, 6)
    print_list(list_head)
    remove_dups_using_dict(list_head)
    print_list(list_head)



