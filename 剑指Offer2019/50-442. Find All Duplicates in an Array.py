"""
Medium

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[2,3]
"""

from typing import List
class Solution:
    def findDuplicates(self, nums: List[int])->List[int]:
        i = 0
        res = set()
        while i < len(nums):
            if nums[i] == i+1:
                i += 1
            elif nums[i] == nums[nums[i]-1]:
                res.add(nums[i])
                i += 1
            else:
                temp = nums[i]
                nums[i], nums[temp-1] = nums[temp-1], temp
        return list(res)

print(Solution().findDuplicates([4, 3, 1, 6, 4, 3]))