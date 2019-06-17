def findCintinuSqu(n):
    res = []
    window = []
    sum = 0
    for i in range(1, n):
        window.append(i)
        sum += i

        while sum > n:
            sum -= window.pop(0)
        if sum == n:
            res.append(window[:])

    return res

print(findCintinuSqu(18))