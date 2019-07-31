"""
长链 m - n 处 与短链一起起步搜索，引用 a is b
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getLen(self, head):
        if not head:
            return 0
        p = head
        count = 0
        while p:
            count += 1
            p = p.next
        return count

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        m = self.getLen(headA)
        n = self.getLen(headB)
        p1, p2 = headA, headB
        if m > n:
            for i in range(m - n):
                p1 = p1.next
        if m < n:
            for i in range(n - m):
                p2 = p2.next
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1