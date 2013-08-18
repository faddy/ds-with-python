from data_structures.stacks import Stack

def move_disk(from_stack, to_stack):
    to_stack.push( from_stack.pop() )


def move_disks(no_of_disks, from_stack, to_stack, using_stack):
    if no_of_disks == 0: return

    move_disks(no_of_disks - 1, from_stack, using_stack, to_stack)
    move_disk(from_stack, to_stack)
    move_disks(no_of_disks - 1, using_stack, to_stack, from_stack)



if __name__ == '__main__':
    no_of_disks = 4

    stackA = Stack()
    for i in reversed(range(no_of_disks)):
        stackA.push(i * 2)

    stackB = Stack()
    stackC = Stack()

    print 'A:', stackA
    print 'B:', stackB
    print 'C:', stackC

    move_disks(no_of_disks, stackA, stackC, stackB)
    print 

    print 'A:', stackA
    print 'B:', stackB
    print 'C:', stackC
