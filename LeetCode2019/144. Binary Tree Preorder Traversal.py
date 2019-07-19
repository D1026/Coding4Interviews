"""
Medium

Given a binary tree, return the preorder traversal of its nodes' values.
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def visitAlongLeftBranch(self, x, res, s):
        while x:
            res.append(x.val)
            if x.right:
                s.append(x.right)
            x = x.left

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        s = [root]
        while s:
            self.visitAlongLeftBranch(s.pop(), res, s)
        return res