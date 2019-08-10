"""
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
# 典型的动态规划，可以用滚动数组来优化空间复杂度到O（n）
# https://www.bilibili.com/video/av60936617?from=search&seid=5329612674935345690
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        matrix = [[None for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    matrix[i][j] = grid[i][j]
                elif i == 0:
                    matrix[i][j] = grid[i][j] + matrix[i][j-1]
                elif j == 0:
                    matrix[i][j] = grid[i][j] + matrix[i-1][j]
                else:
                    matrix[i][j] = grid[i][j] + min(matrix[i][j-1], matrix[i-1][j])

        return matrix[-1][-1]