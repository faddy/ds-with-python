from trees.tree_structures import TreeNode

class NodeWithParent(TreeNode):
    def __init__(self, obj=None):
        super(NodeWithParent, self).__init__(obj)
        self.parent = None

class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self.size = 0


    def length(self):
        return self.size


    def __len__(self):
        return self.size


    def insert(self, value):
        if not value:
            raise Exception('Value cannot be None')
        else:
            node = NodeWithParent(value)
            self._insert(self.root, node)


    def _insert(self, root, node):
        if not root:
            root = node

        elif node.data < root.data:
            self._insert(root.left, node)

        else:
            self._insert(root.right, node)



def create_tree_with_sorted_arr(sorted_arr):
    if not sorted_arr: return None

#    if len(sorted_arr) == 1: return TreeNode(sorted_arr[0])

    mid = len(sorted_arr) / 2
    left_arr = sorted_arr[:mid]
    right_arr = sorted_arr[mid+1:]

    node = TreeNode(sorted_arr[mid])
    node.left = create_tree_with_sorted_arr(left_arr)
    node.right = create_tree_with_sorted_arr(right_arr)

    return node




