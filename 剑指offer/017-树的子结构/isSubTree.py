class TreeNode:
    def __init__(self, x, lc=None, rc=None):
        self.val = x
        self.lc = lc
        self.rc = rc


def search(root, x):
    hots = []
    if not root:
        return hots
    if root.val == x:
        hots.append(root)
    l_hots = search(root.lc, x)
    r_hots = search(root.rc, x)

    return hots + l_hots + r_hots


def isSubtree(a, b):
    if not b:
        return True
    root2 = b.val
    hots = search(a, root2)
    print('--- hots num:', len(hots))

    def compare(x, y):
        if not y:
            return True
        elif not x:
            return False
        else:
            if x.val != y.val:
                return False
            else:
                l_com = compare(x.lc, y.lc)
                r_com = compare(x.rc, y.rc)
                return l_com and r_com

    for r in hots:
        print('---')
        if compare(r, b):
            return True

    return False

a = TreeNode(5, TreeNode(3, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(4)), TreeNode(3))
b = TreeNode(3, TreeNode(1), TreeNode(4))
print(isSubtree(a, b))
"""
遍历，碰到root2.val,递归检查结构是否相同
--- 这个写的太复杂了，没有充分利用递归遍历，参考原版本 ---
"""