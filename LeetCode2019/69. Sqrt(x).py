"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""
"""
求平方根，返回整数，
主体：二分查找搜索根
边界条件：x = 0,1 
搜索范围 [1, x/2], 因为 s^2 >= 2s 从s = 2开始就满足"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x in (0, 1):
            return x
        start = 1
        end = x//2
        ans = 0
        while start <= end:
            m = (start+end) // 2
            s = m**2
            s1 = (m+1)**2

            if s <= x < s1:
                return m
            elif s > x:
                end = m - 1
            elif s < x:
                start = m + 1
                ans = m


print(Solution().mySqrt(10))