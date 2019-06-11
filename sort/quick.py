import numpy as np
def quickSort(x):
    if len(x) <= 1:
        return x
    v = x[0]
    i, j = 1, len(x)-1
    while True:
        while x[i] <= v and i < len(x)-1:
            i += 1
        while x[j] >= v and j > 1:
            j -= 1
        if i >= j:
            break
        x[i], x[j] = x[j], x[i]

    print(x, 'j=', j)
    if x[j] < v:
        x[0], x[j] = x[j], x[0]
        p = j
    else:
        x[0], x[j-1] = x[j-1], x[0]
        p = j-1
    print(x)
    quickSort(x[:p])
    quickSort(x[p+1:])
    return x

print('---', quickSort(np.array([13, 7, 10, 4, 4, 4, 4, 11, 7, 2, 1])))
# --- x[a:b] 是 x 的切片， 而 a = x[a:b], a 是 x[a:b] 的一个拷贝
# 引用作为切片存在， 必须用 numpy.array(), 不开辟额外空间的就地快排 需要在最初调用函数时 传入numpy.array

qs = lambda xs: ((len(xs) <= 1 and [xs]) or [qs([x for x in xs[1:] if x < xs[0]]) + [xs[0]] + qs([x for x in xs[1:] if x >= xs[0]])])[0]
print('---', qs([13, 7, 10, 4, 4, 4, 4, 11, 7, 2, 1]))