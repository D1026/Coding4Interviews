"""
归并排序过程，
"""
def inversePairs(x):
    if len(x) <= 1:
        return 0, x
    parti = len(x)//2
    ln, l = inversePairs(x[:parti])
    rn, r = inversePairs(x[parti:])
    counter = 0
    combine = []
    while l and r:
        if l[-1] > r[-1]:
            counter += len(r)
            combine.insert(0, l.pop())
        elif l[-1] <= r[-1]:
            combine.insert(0, r.pop())

    combine = (l+combine) if l else (r+combine)
    return ln+rn+counter, combine


x = [7, 6, 5, 4, 3, 2, 1]
n, arr = inversePairs(x)
print(n)
print(arr)
