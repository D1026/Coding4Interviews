"""
Medium

Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
# counter计数 O(n), 建堆 O(n), 取topK : k(O(1)+O(log n))

class Solution:
    def topKFrequent(self, nums, k: int):
        from collections import Counter
        import heapq
        count = Counter(nums)
        res = heapq.nlargest(k, count.keys(), key=count.get)
        return res


print(Solution().topKFrequent([3, 4, 5, 5, 2, 1], 2))