class Node(object):
    def __init__(self):
        self.parent = None

def create_tree(N):
    if N < 0:
        return None

    all_nodes = {}

    for level in reversed(range(N+1)):			# for level in [1,0]
        curr_nodes = [Node() for i in range(2**level)]	# [Node()]
        prev_nodes = all_nodes.get(level + 1, None)    # [Node(), Node()] <- all_nodes.get(1, None)

        if prev_nodes:
            i = 0; j = 0
            while i < len(prev_nodes):			# i < 2
                prev_nodes[i].parent = curr_nodes[j]	# prev[0].parent = curr_nodes[0]
                prev_nodes[i+1].parent = curr_nodes[j]     # prev[1].parent = curr_nodes[0]
                i += 2
                j += 1

        all_nodes[level] = curr_nodes			# all_nodes = {1: [Node(), Node()], 2: [N()]}

    return all_nodes[N]					# N=0 -> all_nodes[0]


def create_tree_new(N):
    if N < 0:
        return None

    prev = []
    level = 0

    for level in range(N + 1):
        nodes = []
        for i in range(2**level):
            n = Node()
            n.parent = None if not prev else prev[i/2]
            nodes.append(n)

        prev = nodes


    return prev
