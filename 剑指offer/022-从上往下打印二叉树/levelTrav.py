from collections import deque
class TreeNode:
    def __init__(self, x, lc=None, rc=None):
        self.val = x
        self.lc = lc
        self.rc = rc

def levelTrav(root):
    items = []
    if not root:
        return items
    que = deque([root])
    while que:
        x = que.popleft()
        items.append(x.val)
        if x.lc:
            que.append(x.lc)
        if x.rc:
            que.append(x.rc)

    return items

bt = TreeNode(1,
              TreeNode(2, TreeNode(4, TreeNode(8)), TreeNode(5)),
              TreeNode(3, TreeNode(6), TreeNode(7)))
print(levelTrav(bt))