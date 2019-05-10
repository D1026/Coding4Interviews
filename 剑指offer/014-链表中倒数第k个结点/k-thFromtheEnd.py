class ListNode:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt

def findKthToTail(head, k):
    if not head:
        return None
    fast = head
    slow = head
    for _ in range(k-1):
        if fast.next:
            fast = fast.next
        else:
            return None
    while fast.next:
        fast = fast.next
        slow = slow.next

    return slow

tail = ListNode(1)
head = ListNode(5, ListNode(4, ListNode(3, ListNode(2, tail))))

# 遍历
if head:
    p = head
    print(p.val)
while p.next:
    p = p.next
    print(p.val)
print('---', findKthToTail(head, 4).val)