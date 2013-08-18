
def move_tower(height, from_pole, with_pole, to_pole):
    if height >= 1:
        move_tower(height-1, from_pole, to_pole, with_pole)
        move_disk_stacks(from_pole, to_pole)
        move_tower(height-1, with_pole, from_pole, to_pole)


def move_disk(from_pole, to_pole):
    print 'moving disk from {0} to {1}'.format(from_pole, to_pole)


def move_disk_stacks(from_stack, to_stack):
    to_stack.push(from_stack.pop())


