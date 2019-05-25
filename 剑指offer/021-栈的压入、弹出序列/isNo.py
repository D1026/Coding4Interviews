def isNo(pushSeq, popSeq):
    if len(pushSeq) != len(popSeq):
        return False
    temp = []
    while pushSeq:
        if pushSeq[0] == popSeq[0]:
            pushSeq.pop(0)
            popSeq.pop(0)
        else:
            temp.append(pushSeq.pop(0))
    if not popSeq:
        return True
    else:
        while temp:
            if temp[-1] == popSeq[0]:
                temp.pop()
                popSeq.pop(0)
            else:
                return False
        return True

print(isNo([1,2,3,4,5], [4,5,3,2,1]))
print(isNo([1,2,3,4,5], [4,3,5,1,2]))

"""
模拟入栈过程，遇到出栈序列首元素，弹出"""