from data_structures.linked_lists import Node
from linked_list_problems import utils

#class Node(object):
#    def __init__(self, data):
#        self.data = data
#        self.nxt = None


def rev(head):
    if not head:
        return None
    
    # result needs to be a list because 
    result = []
    _rev(head, result)
    return result[0]


def _rev(head, result):
    if not head.nxt:
        result.append(head)
        return head
    
    temp = _rev(head.nxt, result)
    temp.nxt = head
    head.nxt = None
    return head


#def print_list(head):
#    t = head
#    while t:
#        print str(t.data) + ' ',
#        t = t.nxt


if __name__ == '__main__':
    head = utils.create_unique_linked_list(12)
    utils.print_list(head)
    new_head = rev(head)
    utils.print_list(new_head)
