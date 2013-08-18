from data_structures.stacks import Stack
from data_structures.queues import Queue


def dfs_traversal(tree_node):
    if not tree_node: return []

    stack = Stack()
    stack.push(tree_node)
    result = []

    while not stack.is_empty():
        item = stack.pop()
        result.append(item.data)

        if item.right:
            stack.push(item.right)

        if item.left:
            stack.push(item.left)

    return result


def bfs_traversal(tree_node):
    if not tree_node: return []

    queue = Queue()
    queue.enqueue(tree_node)
    result = []

    while not queue.is_empty():
        item = queue.dequeue()
        result.append(item.data)

        if item.left:
            queue.enqueue(item.left)

        if item.right:
            queue.enqueue(item.right)

    return result
