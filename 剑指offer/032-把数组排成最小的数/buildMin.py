"""
整数转化成字符串
定义大小比较：若 ab < ba, 则 a < b, ab = ba 则 a = b
从小到大拼接
"""

def compare(x, y):
    xy = x+y
    yx = y+x
    if xy < yx:
        return -1
    if xy == yx:
        return 0
    if xy > yx:
        return 1


def build(xs):
    strs = []
    for i in xs:
        strs.append(str(i))
    import functools
    strs.sort(key=functools.cmp_to_key(compare))
    return ''.join(strs)

print(build([3, 32, 321]))
print(build([13, 2, 7, 123]))
