"""
Medium
Given a binary tree, find the leftmost value in the last row of the tree.
Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root) -> int:
        if not root:
            return None
        que = []
        res = []
        que.append(root)
        que.append('#')
        res.append('#')
        while que:
            p = que.pop(0)
            if not que and p == '#':
                break
            if p == '#':
                que.append('#')
                res.append('#')
                continue
            res.append(p.val)
            if p.left:
                que.append(p.left)
            if p.right:
                que.append(p.right)

        for i in range(-1, -len(res)-1, -1):
            if res[i] == '#':
                return res[i+1]


