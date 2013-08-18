from data_structures.stacks import Stack
from trees.tree_structures import TreeNode
import operator

operators = '*+/-'
op_dict   = {'*': operator.mul, '+':operator.add,
             '/': operator.truediv, '-': operator.sub}

def build_parse_tree(expression):
    if not expression:
        return None

    expression = list(expression.replace(' ', ''))
    curr_node = TreeNode()
    stack = Stack()
    stack.push(curr_node)

    for token in expression:
        if token == '(':
            curr_node.left = TreeNode()
            stack.push(curr_node)
            curr_node = curr_node.left

        elif token in operators:
            curr_node.data = token
            curr_node.right = TreeNode()
            stack.push(curr_node)
            curr_node = curr_node.right

        elif token == ')':
            curr_node = stack.pop()

        else:
            # if token is an operand
            curr_node.data = token
            curr_node = stack.pop()

    return curr_node


def evaluate_parse_tree(root):
    if not root:
        return None

    if root.data in operators:
        value1 = evaluate_parse_tree(root.left)
        value2 = evaluate_parse_tree(root.right)
        return _evaluate(root.data, value1, value2)

    else:
        # if root.data is an operand
        return root.data

def _evaluate(op, val1, val2):
    fn = op_dict.get(op)
    try:
        val1 = int(val1)
        val2 = int(val2)
    except:
        pass

    return fn(val1, val2)




