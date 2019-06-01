"""
路径的定义：root->leaf
"""
class TreeNode:
    def __init__(self, x, lc=None, rc=None):
        self.val = x
        self.lc = lc
        self.rc = rc

all = []

def findPath(root, n, pre=[]):
    path = []
    path.extend(pre)
    if not root:
        return
    path.append(root.val)
    n -= root.val
    if n == 0 and not root.lc and not root.rc:
        all.append(path)
        return
    findPath(root.lc, n, path)
    findPath(root.rc, n, path)

    return

tree = TreeNode(7, TreeNode(-3, TreeNode(1), TreeNode(-1)),
                TreeNode(1, TreeNode(0, TreeNode(-3)), TreeNode(-3)))

findPath(tree, 5)
all.sort(key=len, reverse=True)
print(all)