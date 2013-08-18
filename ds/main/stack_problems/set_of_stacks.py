# a set of stacks. create new stack when capacity exceeded

#from stack_implementations import StackWithList
capacity = 3

class SetOfStacks():
    def __init__(self):
        self.storage = [[]]
        self.current = 0

    def push(self, data):
        # if stack at capacity, add another stack, increment current
        if len(self.storage[self.current]) == capacity:
            self.storage.append([])
            self.current += 1

        # add data to current stack
        self.storage[self.current].append(data)

    def pop(self):
        # remove last item from current stack
        if not len(self.storage[self.current]):
            # there are no more items in the set of stacks
            return None

        item = self.storage[self.current].pop()

        # if current stack is empty, remove it, decrement current
        if not len(self.storage[self.current]):
            if self.current > 0:
                del(self.storage[self.current])
                self.current -= 1

        return item
