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

    def merge(self, l, r):

        if l is None:
            return r

        if r is None:
            return l

        if l.val < r.val:
            result = l
            result.next = self.merge(l.next, r)
        else:
            result = r
            result.next = self.merge(l, r.next)
        return result
        # if not l:
        #     return r
        # if not r:
        #     return l
        # p1, p2 = l, r
        # pre2 = None
        #
        # while p1:
        #     while p1.val > p2.val and p2.next:
        #         pre2 = p2
        #         p2 = p2.next
        #
        #     if p2.next is None:
        #         if p1.val > p2.val:
        #             p2.next = p1
        #             return r
        #         else:
        #             p1.next = p2
        #             return r
        #
        #     if pre2 is None:  # head
        #         pre2 = p1
        #         r = pre2
        #         p1 = p1.next
        #         pre2.next.next = p2
        #
        #     else:   # in
        #         pre2.next = p1
        #         p1 = p1.next
        #         pre2.next.next = p2

        # return r

    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if head.next is None:
            return head
        mid = self.mid(head)
        print('--mid: ', mid)
        right = mid.next
        mid.next = None
        head = self.sortList(head)
        right = self.sortList(right)
        return self.merge(head, right)

head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
s = Solution()
head = s.sortList(head)
p = head
while p:
    print(p.val)
    p = p.next

