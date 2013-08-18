class Node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.nxt  = None

    def get_next(self):
        return self.nxt

    def set_next(self, node):
        self.nxt = node

    def get_data(self):
        return self.data

    def set_data(self, newdata):
        self.data = newdata


class UnorderedList(object):
 
    def __init__(self):
        self.head = None


    def get_node_generator(self):
        node = self.head
        while node:
            yield node
            node = node.get_next()


    def _return_last_node(self):
        if not self.head:
            return self.head

        ptr = self.head
        while ptr.get_next():
            ptr = ptr.get_next()

        return ptr


    def is_empty(self):
        return self.head is None


    def length(self):
        if self.is_empty(): return 0
        else:
            count = 0
            ptr = self.head
            while ptr:
                count += 1
                ptr = ptr.get_next()
            return count


    def append(self, item):
        node = Node(item)

        if self.is_empty():
            self.head = node
        else:
            last = self._return_last_node()
            last.set_next(node)


    def insert(self, pos, item):
        if pos < 0 or pos > self.length()+1:
            raise ValueError('Position {0} is outside the limits'.format(pos))

        node = Node(item)

        if pos == 0:
            node.set_next(self.head)
            self.head = node
            return

        p = self.head
        for count in range(pos-1):
            p = p.get_next()

        node.set_next(p.get_next())
        p.set_next(node)


    def pop(self):
        if self.is_empty(): raise Exception('list is empty')

        if self.length() == 1:
            item = self.head.get_data()
            self.head = None
            return item

        p = self.head
        while p.get_next().get_next():
            p = p.get_next()

        item = p.get_next().get_data()
        p.set_next(None)
        return item


    def search(self, item):
        if self.is_empty(): return False

        p = self.head
        while p:
            if p.get_data() == item: return True
            else:
                p = p.get_next()


    def remove(self, item):
        if not self.head: return

        if self.head.get_data() == item:
            self.head = self.head.get_next()

        else:
            p = self.head
            while p.get_next():
                if p.get_next().get_data() == item:
                    p.set_next( p.get_next().get_next() )
                    return
                else:
                    p = p.get_next()


    def index(self, item):
        '''returns the first index of the found item'''
        if self.is_empty():
            return -1

        p = self.head
        i = 0

        while p:
            if p.get_data() == item:
                return i
            else:
                p = p.get_next()
                i += 1

        # didn't find the item in the linked list
        return -1 




