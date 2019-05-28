def isBST(sque):
    if len(sque) <= 1:
        return True
    root = sque[-1]
    for i in range(len(sque)):
        if sque[i] > root:
            break
    for j in range(i, len(sque)):
        if sque[j] < root:
            return False
    return isBST(sque[:i]) and isBST(sque[i:-1])


print(isBST([1, 4, 3, 5, 7]))
print(isBST([1, 6, 5, 8, 9, 7]))