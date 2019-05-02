def getMin (array):
    if len(array) == 0:
        return 0
    l = 0
    r = len(array) - 1
    mid = (l+r)//2
    while True:
        if r == l+1:
            return array[r]
        if array[mid] >= array[l]:
            l = mid
        else:
            r = mid
        mid = (l+r)//2

print(getMin([4, 5, 6, 1, 2]))
print(getMin([5, 3, 4]))
print(getMin([7, 7]))
