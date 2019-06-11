def MoreThanHalfNum_Solution(numbers):
    # write code here
    res = None
    cnt = 0
    for i in numbers:  # 留下数组中出现次数最高的数  --- 这个表述不对，这种方法留下的未必是最小，但对于解体不影响
        if not res:
            res = i
            cnt = 1
        else:
            if i == res:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    res = None
    # 判断次数是否大于一半
    cnt = 0 
    for i in numbers:
        if i == res:
            cnt += 1
    if cnt > len(numbers) / 2:
        return res
    else:
        return 0

print(MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))
print(MoreThanHalfNum_Solution([1,0,3,0,0,0,5,4,0]))
