class ListNode:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt

def traverse(head):
    if head:
        p = head
        print(p.val)
    while p.next:
        p = p.next
        print(p.val)
    print('--- end traversing ---')

def inverse(head):
    if not head or not head.next:
        return head
    h = head
    tail = head
    p = head.next
    while tail.next:
        tail.next = p.next
        p.next = h
        h = p
        p = tail.next

    return h

head = ListNode('A', ListNode('B', ListNode('C', ListNode('D', ListNode('E', ListNode('F'))))))
traverse(head)
traverse(inverse(head))