class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        if self.out_stack:
            return self.out_stack.pop()
        else:
            return None

    def __len__(self):
        return len(self.in_stack)+len(self.out_stack)


queue = Queue()
queue.push(5)
queue.push(7)
queue.push(1)
print(queue.pop())
print(len(queue))