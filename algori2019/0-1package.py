import numpy as np


def solve(vlist, wlist, cap):
    totalLength = len(vlist)
    resArr = np.zeros((totalLength+1, cap+1), dtype=np.int32)

    vlist.insert(0, 0)
    wlist.insert(0, 0)  # 占位，使 i, j 与 v,w-list中对齐
    for i in range(1, totalLength+1):
        for j in range(1, cap+1):
            if wlist[i] <= j:
                resArr[i, j] = max(resArr[i-1, j-wlist[i]] + vlist[i], resArr[i-1, j])
            else:
                resArr[i, j] = resArr[i-1, j]
    return resArr[-1, -1]


if __name__ == '__main__':
    v = [60, 100, 120]
    w = [10, 20, 30]
    cap = 50
    result = solve(v, w, cap)
    print(result)
