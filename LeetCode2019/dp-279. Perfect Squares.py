"""
Medium

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

# 动态规划 Dynamic programming
class Solution:
    def numSquares(self, n: int) -> int:
        f = [x for x in range(n+1)]
        for i in range(1, n+1):
            j = 1
            while j**2 <= i:
                f[i] = min(f[i], f[i-j**2]+1)
                j += 1
        return f[n]

# BFS，