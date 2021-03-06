"""
Medium
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Note: A leaf is a node with no children.
Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        path = []
        left = []
        right = []
        if not root.left and not root.right:
            if sum == root.val:
                path.append([root.val])
            return path
        if root.left:
            left = self.pathSum(root.left, sum - root.val)
        if root.right:
            right = self.pathSum(root.right, sum - root.val)

        return [[root.val] + x for x in (left + right)]