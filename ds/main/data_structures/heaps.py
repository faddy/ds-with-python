import heapq


class MinHeap(object):

    def __init__(self):
        self.values = []


    def push(self, val):
        heapq.heappush(self.values, val)


    def pop(self):
        if self.size() == 0:
            return None

        return heapq.heappop(self.values)


    def size(self):
        return len(self.values)


    def peek(self):
        if self.values:
            return self.values[0]



class MaxHeap(object):

    def __init__(self):
        self.values = []


    def push(self, val):
        heapq.heappush(self.values, -val)


    def pop(self):
        if self.size() == 0:
            return None

        val = heapq.heappop(self.values)
        return -val


    def size(self):
        return len(self.values)


    def peek(self):
        if self.values:
            return -(self.values[0])
