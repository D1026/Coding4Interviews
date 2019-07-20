"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def goAlongLeftBranch(self, root, s):
        x = root
        while x:
            s.append(x)
            x = x.left

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return None
        s = []
        self.goAlongLeftBranch(root, s)
        res = []
        while s:
            x = s.pop()
            res.append(x.val)
            if len(res) == k:
                break
            if x.right:
                self.goAlongLeftBranch(x.right, s)

        return res[-1]