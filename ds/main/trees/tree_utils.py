from tree_structures import TreeNode, BinaryTree


def make_tree(arr):
    if not arr: return None
    if len(arr) == 1: return TreeNode(arr[0])

    mid = (len(arr)-1)/2
    node = TreeNode(arr[mid])
    node.left = make_tree(arr[:mid])
    node.right = make_tree(arr[mid+1:])
    return node


def make_tree_from_sorted_array(arr):
    return BinaryTree( make_tree(arr) )


def test():
    bt = make_tree_from_sorted_array([-1,2,4,5,7,9])
    print bt.inorder()
    print bt.preorder()
    print

    bt1 = make_tree_from_sorted_array([3])
    print bt1.inorder()

if __name__ == '__main__':
    test()
