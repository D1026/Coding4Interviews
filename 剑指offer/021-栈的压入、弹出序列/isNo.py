def validateStackSequences(pushed, popped) -> bool:
    if len(pushed) < len(popped):
        return False
    stack = []
    while pushed:
        stack.append(pushed.pop(0))
        while stack and stack[-1] == popped[0]:
            stack.pop()
            popped.pop(0)
    while popped:
        if popped[0] == stack[-1]:
            stack.pop()
            popped.pop(0)
        else:
            return False
    return True

print(validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
print(validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))

"""
模拟入栈过程，遇到出栈序列首元素，弹出"""