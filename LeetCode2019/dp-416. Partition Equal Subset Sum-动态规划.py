"""
Medium

Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.

Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution:
    def canPartition(self, nums) -> bool:
        # 计算总价值
        c = sum(nums)
        # 奇数直接排除
        if c % 2 != 0:
            return False
        c = c // 2
        w = [False] * (c + 1)
        # 第0个位置设置为true，表示当元素出现的时候让w[i-num]为True,也就是w[i]为True
        w[0] = True
        for num in nums:
            for i in range(c, num - 1, -1):
                w[i] = w[i] or w[i - num]   # 不是很理解， 为什么是 w[i]也就是w[i+1] or ..
        return w[c]