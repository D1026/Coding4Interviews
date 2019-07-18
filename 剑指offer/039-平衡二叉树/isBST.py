"""
利用后序遍历，自下而上，每个节点只用计算一次其深度，
（想了想这种写法根本没意义，递归每个也是每个节点算一次）
"""


class TreeNode:
    def __init__(self, x, lc=None, rc=None):
        self.val = x
        self.lc = lc
        self.rc = rc

def gotoHLVFL(nodeStack):
    while nodeStack[-1]:
        x = nodeStack[-1]
        if x.lc:
            if x.rc:
                nodeStack.append(x.rc)
            nodeStack.append(x.lc)
        else:
            nodeStack.append(x.rc)
    nodeStack.pop()

def travPost(root):
    sequ = []
    if not root:
        return sequ
    x = root
    pStack = []
    pStack.append(x)
    while pStack:
        if x not in [pStack[-1].lc, pStack[-1].rc]:
            gotoHLVFL(pStack)
        sequ.append(pStack.pop().val)

    return sequ

# --------------------------------'
"""
递归式，平衡返回深度，不平衡返回-1
Runtime: 48 ms, faster than 98.82% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 17.8 MB, less than 87.20% of Python3 online submissions for Balanced Binary Tree.
"""

def getDeep(x):
    if x is None:
        return 0
    left = getDeep(x.left)
    if left == -1:
        return -1
    right = getDeep(x.right)
    if right == -1:
        return -1
    return -1 if abs(left-right) > 1 else 1 + max(left, right)

def isBST(root):
    return getDeep(root) != -1
