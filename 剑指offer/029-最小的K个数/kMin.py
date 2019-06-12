# 快排划分
def kMin(x, k):
    v = x[0]
    pre = [les for les in x if les < v]
    mid = [mid for mid in x if mid == v]
    post = [mor for mor in x if mor > v]

    if len(pre) > k:
        return kMin(pre, k)
    elif len(pre) == k:
        return pre
    else:
        return pre+kMin(pre, k-len(pre))

a = [7,6,5,4,3,2,1]
print(kMin(a, 3))

# 建立最小堆