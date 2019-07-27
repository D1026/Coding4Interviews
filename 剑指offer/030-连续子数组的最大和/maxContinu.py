# 扫描
def maxContinu1(x):
    sum = 0
    candid = []
    s, e = 0, 0
    for i in range(len(x)):
        if x[i] >= 0:
            sum += x[i]
            e = i
        else:
            candid.append([sum, s, e])
            sum += x[i]
            e = i
            if sum < 0:
                s, e = i+1, i+1
                sum = 0
    import numpy as np
    candid = np.array(candid)
    maxConti = candid[candid.argmax(0)[0]]
    return maxConti

print(maxContinu1([-1, 2, 4, 1, 0, -3]))

# 动态规划 --- 下面答案是错的
def maxContinuSum(x):
    sum = 0
    for i in range(len(x)):
        if i == 0 or sum <= 0:
            sum = x[i]
        elif x[i] > 0:
            sum += x[i]
        else:
            pass
        # print(sum)
    return sum

print(maxContinuSum([-1, 2, 4, 1, 0, -3, 5]))
