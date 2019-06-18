"""
约瑟夫环，
思路1：环形链表模拟
思路2：递推公式
f(n, m) = 0,    n=1
          [f(n-1, m) + m] % n,  n>1
"""

def lastRemain(n, m):
    if n < 1 or m < 1:
        return None
    last = 0
    for i in range(2, n+1):
        last = (last+m) % i

    return last

print(lastRemain(5, 3))