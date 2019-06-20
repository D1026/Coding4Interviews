"""
利用双向队列，最大值下标保存在 que[0]
"""


def getMax(a, n):
    if not n:
        return None
    if n == 1:
        return a

    que = []
    res = []
    for i in range(len(a)):
        while que and que[0] <= i-n:
            que.pop(0)
        while que and a[que[-1]] <= a[i]:
            que.pop()
        que.append(i)

        if i < n-1:
            continue
        res.append(a[que[0]])

    return res

print(getMax([1, 2, 3, 4, 5, 6, 17, 7], 3))