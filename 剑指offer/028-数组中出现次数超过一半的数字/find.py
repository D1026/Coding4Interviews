# 基于快排寻找中位数 O(n), 就是寻找第 k 大的数
def find1(x, k):
    v = x[0]
    pre = [les for les in x if les < v]
    post = [mor for mor in x if mor > v]
    mid = [mid for mid in x if mid == v]
    if len(pre) < k and len(pre+mid) >= k:
        return v
    elif len(pre) >= k:
        return find1(pre, k)
    else:
        return find1(post, k-len(pre+mid))

a = [8, 4, 5, 4, 4, 5, 7, 4, 4]
print(find1(a, len(a)//2))
# 对对碰方法
