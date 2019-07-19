"""
Hard

Given a binary tree, return the postorder traversal of its nodes' values.
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Runtime: 36 ms, faster than 65.68% of Python3
# Memory Usage: 13.2 MB, less than 29.97%

class Solution:
    def gotoHLVFL(self, s):
        while s[-1]:
            x = s[-1]
            if x.left:
                if x.right:
                    s.append(x.right)
                s.append(x.left)
            else:
                s.append(x.right)

        s.pop()

    def postorderTraversal(self, root):
        if not root:
            return []
        x = root
        s = [x]
        res = []

        while s:
            if s[-1].left != x and s[-1].right != x:
                self.gotoHLVFL(s)
            x = s.pop()
            res.append(x.val)

        return res