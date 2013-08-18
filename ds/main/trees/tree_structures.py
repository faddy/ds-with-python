
class TreeNode(object):
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, rootnode=None):
        self.root = rootnode

    def inorder(self):
        if not self.root: return
        else:
            out = []
            self.__inorder(self.root, out)
            return out

    def preorder(self):
        if not self.root: return
        else: 
            out = []
            self.__preorder(self.root, out)
            return out

    def postorder(self):
        if not self.root: return
        else:
            out = []
            self.__postorder(self.root, out)
            return out

    def search(self, num):
        if num is None: return True # None value will always be there
        if not self.root: return False
        else:
            return self.__search(self.root, num)

    def get_list_of_nodes_per_level(self):
        if not self.root: return None

        l = []
        l.append([self.root])
        lvl = 0
        while True:
            item = l[lvl]
            newl = []
            for node in item:
                if node.left: newl.append(node.left)
                if node.right: newl.append(node.right)

            if newl:
                l.append(newl)
                lvl += 1
            else:
                break

        return l

    def common_ancestor(self, p, q):
        if not self.root: return None
        if not p or not q: return None

        return self.__common_ancestor(self.root, p, q)

    def find_sum(self, total):
        if not self.root: return None
        else:
            self.__find_sum(self.root, total, path=[])

    def __find_sum(self, node, total, path):
        if not node: return
        t = total - node.data
        npath = path + [node.data]
        if not (node.left or node.right):
            if t == 0: print npath
            return

        self.__find_sum(node.left, t, npath)
        self.__find_sum(node.right, t, npath)

    def __common_ancestor(self, node, p, q):
        if self.__covers(node.left, p) and self.__covers(node.left, q):
            return self.__common_ancestor(node.left, p, q)
        elif self.__covers(node.right, p) and self.__covers(node.right, q):
            return self.__common_ancestor(node.right, p, q)
        else:
            return node

    def __covers(self, node, p):
        if not node: return False
        if node.data == p: return True
        return self.__covers(node.left, p) or self.__covers(node.right, p)


    def __inorder(self, node, out):
        if not node: return
        self.__inorder(node.left, out)
        out.append(node.data)
        self.__inorder(node.right, out)

    def __preorder(self, node, out):
        if not node: return
        out.append(node.data)
        self.__preorder(node.left, out)
        self.__preorder(node.right, out)

    def __postorder(self, node, out):
        if not node: return
        self.__postorder(node.left, out)
        self.__postorder(node.right, out)
        out.append(node.data)

    def __search(self, node, num):
        if not node: return False
        if node.data == num: return True
        else:
            return self.__search(node.left, num) or self.__search(node.right, num)


class BinarySearchTree(BinaryTree):
    def search(self, num):
        if num is None: return True
        if not self.root: return False
        else:
            return self.__search(self.root, num)

    def insert(self, num):
        if num is None: return False
        elif not self.root: 
            self.root = TreeNode(num)
        else:
            self.__insert(self.root, num)

    def __search(self, node, num):
        if not node: 
            return False

        if num == node.data: 
            return True
        elif num < node.data:
            return self.__search(node.left, num)
        else:
            return self.__search(node.right, num)

    def __insert(self, node, num):
        if num < node.data:
            if not node.left: node.left = TreeNode(num)
            else: self.__insert(node.left, num)

        else:
            if not node.right: node.right = TreeNode(num)
            else: self.__insert(node.right, num)


def create_test_tree():
    tree = BinarySearchTree()
    tree.root = TreeNode(5)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(7)
    n = tree.root.left
    n.left = TreeNode(1)
    n.right = TreeNode(4)
    n = tree.root.right
    n.right = TreeNode(15)
    return tree

def tree_test():
    tree = create_test_tree()
    print tree.inorder()
    print tree.preorder()
    print tree.postorder()

