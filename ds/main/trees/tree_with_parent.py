import tree_structures as tr

class TreeNodeWithParent(tr.TreeNode):
    def __init__(self, d):
        super(TreeNodeWithParent, self).__init__(d)
        self.parent = None
