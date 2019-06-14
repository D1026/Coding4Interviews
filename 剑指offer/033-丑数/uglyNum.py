"""

"""
def getUglyNum(n):
    if n <= 0:
        return 0
    ugs = [1]
    p2 = 0
    p3 = 0
    p5 = 0
    while len(ugs) < n:
        nxt = min(ugs[p2]*2, ugs[p3]*3, ugs[p5]*5)
        ugs.append(nxt)
        while ugs[p2]*2 <= ugs[-1]:
            p2 += 1
        while ugs[p3]*3 <= ugs[-1]:
            p3 += 1
        while ugs[p5]*5 <= ugs[-1]:
            p5 += 1
    return ugs[-1]

print(getUglyNum(0))
print(getUglyNum(4))
print(getUglyNum(5))
print(getUglyNum(6))
print(getUglyNum(7))
