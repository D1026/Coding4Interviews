"""
Medium
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def mid(self, h):
        # len(h) 至少为2
        slow, fast = h, h
        while fast.next.next:
            slow = slow.next
            fast = fast.next
        return slow

    def merge(self, ):

    def sortList(self, head: ListNode) -> ListNode:
        mid = self.mid(head)
        right = mid.next
        mid.next = None
        self.sortList(head)
        self.sortList(right)
        return self.merge()

