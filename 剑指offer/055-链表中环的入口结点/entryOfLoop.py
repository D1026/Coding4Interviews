class ListNode:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt

def meetNode(head):
    """
    判断是否有环，并找出环内一点
    :param head:
    :return:
    """
    if not head:
        return None
    fast, slow = head, head
    while fast.next and fast.next.next and slow.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return fast
    return None

def entryOfLoop(head):
    p = meetNode(head)
    if not p:
        return None
    loop = p
    count = 0
    while True:
        loop = loop.next
        count += 1
        if loop == p:
            break
    fast, slow = head, head
    for i in range(count):
        fast = fast.next
    while fast != slow:
        fast = fast.next
        slow = slow.next

    return fast

b = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
a = ListNode(6)
b.next.next.next.next.next = a
a.next = b.next.next    # 3

print(entryOfLoop(b).val)