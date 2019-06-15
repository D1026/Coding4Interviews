class TreeNode:
    def __init__(self, x, lc=None, rc=None):
        self.val = x
        self.lc = lc
        self.rc = rc

def getDepth(root):
    if not root:
        return 0
    if not root.lc and not root.rc:
        return 1
    depth = 1 + max(getDepth(root.lc), getDepth(root.rc))
    return depth

tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(6))))
print(getDepth(tree))