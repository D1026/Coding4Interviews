"""
Medium
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

class Solution(object):
    def searchRange(self, nums, target):
        res = [-1, -1]
        if not nums:
            return res
        if len(nums) == 1:
            if nums[0] == target:
                res = [0, 0]
            return res
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] == target:
                res[0] = l
                break
            if nums[r] == target:
                res[0] = r
            m = (l+r)//2
            if nums[m] < target:
                l = m+1
            if nums[m] >= target:
                r = m

        r = len(nums)-1
        while l < r:
            if nums[l] == target:
                res[1] = l
            if nums[r] == target:
                print('---')
                res[1] = r
                break
            m = (l+r) // 2
            if nums[m] <= target:
                l = m
            if nums[m] > target:
                r = m-1
        return res

print(Solution().searchRange([5,7,7,8,8,10], 8))

# 还是有问题，边界条件太不好控制了， 既然都是整数 不如用插入法找到 target-0.5、target+0.5 的位置