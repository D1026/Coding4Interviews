"""先序遍历 + 空指针标记
进行序列化和反序列化
"""

class TreeNode:
    def __init__(self, x, lc=None, rc=None):
        self.val = x
        self.lc = lc
        self.rc = rc
class Solution:

    def __init__(self):
        self.index = -1

    def serialize(self, root):
        x = []
        if not root:
            x.append('$')
            return x
        if root:
            x.append(root.val)
            return x + self.serialize(root.lc) + self.serialize(root.rc)

    def rebuid(self, x):
        if not x:
            root = None

        self.index += 1
        if self.index >= len(x):
            return None
        if x[self.index] != '$':
            root = TreeNode(x[self.index])
            root.lc = self.rebuid(x)
            root.rc = self.rebuid(x)

        else:
            return None
        return root


sol = Solution()
tree = sol.rebuid([1, 2, '$', '$', 3, 4, '$', '$',  5, '$', '$'])
print(sol.serialize(tree))
