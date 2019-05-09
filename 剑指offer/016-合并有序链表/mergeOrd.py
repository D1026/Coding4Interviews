class ListNode:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt

class LinkedList:
    def __init__(self):
        self.h = None
        self.t = None

    def __add__(self, other):
        self.t.next = other
        return self.h

    def append(self, x):
        if not self.h:
            self.h = x
            self.t = x
        else:
            self.t.next = x
            self.t = x

def traverse(head):
    if head:
        p = head
        print(p.val)
    while p.next:
        p = p.next
        print(p.val)
    print('--- end traversing ---')

def merge(list0, list1):
    p0 = list0
    p1 = list1
    mer = LinkedList()
    while not p0 and not p1:
        if p0.val > p1.val:
            mer.append(ListNode(p1.val))
            p1 = p1.next
        else:
            mer.append(ListNode(p0.val))
            p0 = p0.next
    # --
    traverse(p0)
    traverse(p1)
    if p0:
        mer += p0
    if p1:
        mer += p1
    return mer

a = ListNode(2, ListNode(5, ListNode(7, ListNode(10, ListNode(17)))))
b = ListNode(4, ListNode(5, ListNode(6)))
ab = merge(a, b)
traverse(ab)