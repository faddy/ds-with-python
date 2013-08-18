

class BinaryHeap(object):
    """
    Max heap implementation
    """

    def __init__(self):
        self.heaplist = [0]
        self.heapsize = 0


    def insert(self, k):
        self.heaplist.append(k)
        self.heapsize += 1
        self._perc_up(self.heapsize)


    def peek_max(self):
        return self.heaplist[1]


    def pop_max(self):
        max_item = self.heaplist[1]
        self.heaplist[1] = self.heaplist[-1]
        self.heapsize -= 1
        self._perc_down(1)


    def is_empty(self):
        return self.heapsize == 0


    def size(self):
        return self.heapsize


    def build_heap(self, alist):
        pass


    def _perc_up(self, i):
        while i/2 > 0:
            if self.heaplist[i] > self.heaplist[i/2]:
                self.swap(self.heaplist, i, i/2)
            i /= 2


    def _perc_down(self, i):
        while i*2 <= self.heapsize:
            largest = self.max_child(i)


    def max_child(self, i):
        left = self.heapsize[2*i]
        right = self.heapsize[2*i + 1]
        largest = i
        if self.heaplist[i] < self.heaplist[left]:
            largest = left
        if largest < right:
            largest = right


    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
