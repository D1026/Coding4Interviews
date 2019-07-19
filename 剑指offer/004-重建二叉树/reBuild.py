
class BiTreeNode:
    def __init__(self, x):
        self.val = x
        self.lc = None
        self.rc = None

def reBuild(pre, inorder):
    if not pre:
        return None
    val = pre[0]
    root = BiTreeNode(val)

    for i in range(len(inorder)):
        if val == inorder[i]:
            break

    root.lc = reBuild(pre[1:i+1], inorder[0:i])
    root.rc = reBuild(pre[i+1:], inorder[i+1:])

    return root

def inorder(tree):
    if tree is None:
        return
    inorder(tree.lc)
    print(tree.val)
    inorder(tree.rc)

inorder(reBuild(['a', 'b', 'd', 'c'], ['d', 'b', 'a', 'c']))