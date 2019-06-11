# 基于快排寻找中位数 O(n), 就是寻找第 len(x)//2 大的数
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

a = [8, 4, 5, 4, 4, 5, 7, 4, 4, 10, 4]
print(find1(a, len(a)//2))

# 对对碰方法
def find2(x):
    num = None
    cot = 0
    for i in x:
        if not num:
            num = i
            cot = 1
        else:
            if num == i:
                cot += 1
            else:
                cot -= 1
            if cot == 0:
                num = None
    # 是否超过一半
    times = 0
    for i in x:
        if i == num:
            times += 1
    if times > len(x)//2:
        return num
    else:
        return None


print(find2(a))
print(find2([1, 2, 3, 4, 5]))
