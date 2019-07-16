"""
Easy

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

# 方法1：排序，取中位数 O( N logN )；方法二：对对碰，i，i+1，不一样就抵消，一样累计 O(N)
class Solution:
    def majorityElement(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        candidate = None
        count = 0
        for i in nums:
            if candidate == i:
                count += 1
            elif count > 0:
                count -= 1
            else:
                candidate, count = i, 1
        return candidate


