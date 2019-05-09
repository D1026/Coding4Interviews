class ListNode:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt


def FindKthToTail(head, k):
    # write code here
    if not head: return None
    fast_p = head
    slow_p = head
    for _ in range(k):
        if fast_p:  # 这里他用了哨兵
            fast_p = fast_p.next
        else:
            return None
    while fast_p:
        fast_p = fast_p.next
        slow_p = slow_p.next
    return slow_p

# --- test ---
tail = ListNode(1)
head = ListNode(5, ListNode(4, ListNode(3, ListNode(2, tail))))
# 遍历
if head:
    p = head
    print(p.val)
while p.next:
    p = p.next
    print(p.val)

print('---', FindKthToTail(head, 4).val)