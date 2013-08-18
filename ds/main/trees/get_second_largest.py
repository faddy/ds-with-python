import sys
from trees.tree_structures import TreeNode

def get_second_max(node):
    max_node = get_max(node)
    second_max = get_max(node, max_node)
    return second_max.data
    

def get_max(node, skip_node=None):
    if not node: return None

    if not node.left and not node.right: 
        if skip_node and node == skip_node:
            return None
        else:
            return node
        
    left_max = None
    right_max = None
        
    if node.left:
        left_max = get_max(node.left, skip_node)        
        
    if node.right:
        right_max = get_max(node.right, skip_node)      
    
    
    if skip_node and node == skip_node:
        largest = TreeNode(-sys.maxint)
    else:
        largest = node
            
    if left_max and left_max.data > largest.data: 
        largest = left_max
        
    if right_max and right_max.data > largest.data:
        largest = right_max
    
    return largest


def make_tree():
    root = TreeNode(30)
    root.left = TreeNode(1)
    root.right = TreeNode(10)
    root.left.left = TreeNode(30)
    root.left.right = TreeNode(24)
    root.right.right = TreeNode(5)
    return root


def inorder_tree(node):
    if not node: return

    inorder_tree(node.left)
    print node.data, ' ',
    inorder_tree(node.right)


