from data_structures import heaps


class Values(object):

    def __init__(self):
        self.left = heaps.MaxHeap()
        self.right = heaps.MinHeap()
        self.median = None


    def add_value(self, val):
        median = self.get_median()

        if not median or val <= median:
            # push to left heap
            self.left.push(val)
            self.balance_heaps()

        else:
            # push to right heap
            self.right.push(val)
            self.balance_heaps()


    def balance_heaps(self):
        diff = self.left.size() - self.right.size() 

        if -1 <= diff <= 1:
            return

        elif diff > 1: # left > right
            # move item from left to right
            max_item = self.left.pop()
            self.right.push(max_item)
        
        else:	       # right > left
            # move item from right to left
            min_item = self.right.pop()
            self.left.push(min_item)


    def get_median(self):
        l = self.left.size()
        r = self.right.size()

        if l == r:
            if l == 0: return None
            else: return float(self.left.peek() + self.right.peek()) / 2

        elif l > r:
            return self.left.peek()

        else:
            return self.right.peek()
