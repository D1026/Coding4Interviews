# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getDeep(self, x):
        if x is None:
            return 0
        left = self.getDeep(x.left)
        if left == -1:
            return -1
        right = self.getDeep(x.right)
        if right == -1:
            return -1
        return -1 if abs(left - right) > 1 else 1 + max(left, right)

    def isBalanced(self, root) -> bool:
        return self.getDeep(root) != -1
