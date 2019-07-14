"""
Medium
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n^2.
"""


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        import heapq
        queue, m, n = [(matrix[0][0], 0, 0)], len(matrix[0]), len(matrix)   # 堆中元素为元组，直接按元组<方法比较
        for i in range(k):
            mymin, i, j = heapq.heappop(queue)
            if i == 0 and j + 1 < m:
                heapq.heappush(queue, (matrix[i][j + 1], i, j + 1))
            if i + 1 < n:
                heapq.heappush(queue, (matrix[i + 1][j], i + 1, j))
        return mymin