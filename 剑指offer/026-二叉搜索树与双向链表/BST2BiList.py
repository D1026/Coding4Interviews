"""
中序遍历，左右指针串联
"""
class TreeNode:
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.lc = l
        self.rc = r

def convert(root):
    if not root:
        return None
    stack = []
    head = None
    pre = None
    p = root
    while p or stack:
        while p:
            stack.append(p)
            p = p.lc

        p = stack.pop()
        if not head:
            head = p
            pre = p
        else:
            pre.rc = p
            p.lc = pre
            pre = p

        p = p.rc

    return head

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5, r=TreeNode(6)))
head = convert(root)
p = head
print(p.rc.rc.rc.rc.lc.val, '4')
while p:
    print(p.val)
    p = p.rc