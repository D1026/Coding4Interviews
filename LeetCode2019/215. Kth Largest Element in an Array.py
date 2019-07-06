"""
215. Kth Largest Element in an Array
Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

"""
思路1、使用快排划分，
思路2、使用最大堆
剪纸offer-29"""
# class Solution:
#     def findKthLargest(self, nums, k):
#         if len(nums) < k:
#             return None
#         v = nums[0]
#         les = []
#         mor = []
#         for e in nums[1:]:
#             if e >= v:
#                 mor.append(e)
#             else:
#                 les.append(e)
#         if len(mor) >= k:
#             return self.findKthLargest(mor, k)
#         if len(mor) == k-1:
#             return v
#         if len(mor) < k-1:
#             return self.findKthLargest(les, k-len(mor)-1)
#
# print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))

# 快慢指针qsort
class Solution:
    def findKthLargest(self, nums, k):
        def partition(nums, l, r):
            pivot = nums[l]
            i = l
            for j in range(l+1, r+1):
                if nums[j] < pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[i] = nums[i], nums[l]
            return i

        if not nums or len(nums) < k:
            return None

        l = 0
        r = len(nums)-1
        while True:
            pivot_index = partition(nums, l, r)
            if pivot_index == len(nums)-k:
                return nums[pivot_index]
            if pivot_index < len(nums)-k:
                l = pivot_index + 1
                continue
            if pivot_index > len(nums)-k:
                r = pivot_index - 1

print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))