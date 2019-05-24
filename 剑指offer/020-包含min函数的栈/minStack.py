"""
使用一个辅助栈，存储当前最小值，数据栈与min栈长度始终对齐
"""
class StackWithMin:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x):
        self.stack.append(x)
        if not self.minStack:
            self.minStack.append(x)
        elif x < self.minStack[-1]:
            self.minStack.append(x)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self):
        self.minStack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.minStack[-1]
