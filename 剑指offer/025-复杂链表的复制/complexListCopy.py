class complexListNode:
    def __init__(self, x, nx=None, rx=None):
        self.val = x
        self.next = nx
        self.rand = rx

def copy(head):
    if not head:
        return None
    p = head
    while p:
        pCopy = complexListNode(p.val, p.next)
        p.next = pCopy
        p = pCopy.next
    p = head
    while p:
        p.next.rand = p.rand.next if p.rand else None
        p = p.next.next
    p = head
    newHead = head.next
    while p:
        successor = p.next
        p.next = successor.next if successor else None
        p = successor

    return newHead

a = complexListNode(1, complexListNode(2, complexListNode(3, complexListNode(4, complexListNode(5)))))
a.next.rand = a.next.next.next  # 2.rand->4
b = copy(a)
p = b
while p:
    print('val: ', p.val, 'rand.val: ', p.rand.val if p.rand else None)
    p = p.next