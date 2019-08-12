"""
Medium

Given an unsorted array of integers, find the length of longest increasing subsequence.
Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
# 普通动态规划 O（n^2), 二分+DP O（N logN)：https://www.bilibili.com/video/av60528477?from=search&seid=15316495741417392069

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1]* len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)  # dp[i] 为以 i 结尾的最大子数组长度

