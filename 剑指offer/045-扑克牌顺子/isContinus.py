def isContinuous(x):
    x.sort()
    gaps = 0
    zeros = 0
    for i in range(5):
        if x[i] == 0:
            zeros += 1
        else:
            break

    for j in range(i, 4):
        # print('this')
        if x[j+1] == x[j]:
            return False
        else:
            gaps += x[j+1] - x[j] - 1
    if zeros >= gaps:
        return True
    else:
        return False

print(isContinuous([0, 0, 0, 0, 9]))
print(isContinuous([0, 0, 0, 5, 9]))
print(isContinuous([0, 0, 6, 5, 9]))
print(isContinuous([6, 8, 7, 5, 9]))