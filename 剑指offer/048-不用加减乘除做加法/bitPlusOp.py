"""
位异或 + 位进位，直到没有进位
"""


def add(n1, n2):
    from ctypes import c_int
    while n2 != 0:
        temp = c_int(n1 ^ n2).value
        n2 = c_int((n1 & n2) << 1).value    # 进位
        n1 = temp
    return n1


print(add(7, 18))
print(add(-3, 10))
