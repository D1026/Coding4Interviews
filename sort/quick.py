def quickSort(x):
    if len(x) <= 1:
        return x
    v = x[-1]
    i, j = 0, len(x)-2
    while i < j:
        while i < j:
            if x[i] > v:
                break
            else:
                i += 1
        while i < j:
            if x[j] < v:
                break
            else:
                j -= 1
        x[i], x[j] = x[j], x[i]

    p = i if i <= j else j
    while p < len(x)-1:
        if x[p] >= v:
            x[p], x[-1] = x[-1], x[p]
            break
        else:
            p += 1
    print(x)
    quickSort(x[:p])
    quickSort(x[p+1:])
    return x

print('---', quickSort([6, 3, 2, 2, 1]))
