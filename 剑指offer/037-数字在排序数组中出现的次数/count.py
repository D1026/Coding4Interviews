"""
二分查找，找到头尾 i, j
"""
def countN(x, n):
    start, end = 0, -1

    i, j = 0, len(x) - 1
    while j > i+1:
        ml = (i+j)//2
        if x[ml] < n:
            i = ml
        if x[ml] >= n:
            j = ml
        if x[j] == n and (j == 0 or x[j-1] < n):
            start = j
            break

    i, j = 0, len(x) - 1
    while j > i + 1:
        mr = (i + j) // 2
        if x[mr] <= n:
            i = mr
        if x[mr] > n:
            j = mr
        if x[i] == n and (i == len(x)-1 or x[i+1] > n):
            end = i
            break
    print('start: ', start, ' end: ', end)
    return (end-start+1)

print(countN([1, 3, 5, 5, 7, 7, 7, 8], 7))
print(countN([1, 3, 5, 5, 7, 7, 8], 1))
print(countN([1, 3, 5, 5, 7, 7, 7, 8], 9))