"""
位异或 + 位进位，直到没有进位
"""
from ctypes import c_int
print(bin(7))
print(bin(7 >> 3))
print(bin(7 & 3))
print(bin(18))
print(bin(7 ^ 18))
print((7 ^ 18))
print(c_int(7 ^ 18))


def add(n1, n2):
    from ctypes import c_int
    while n2 != 0:
        temp = c_int(n1 ^ n2).value
        n2 = c_int((n1 & n2) << 1).value    # 进位
        n1 = temp
    return n1

print(add(7, 18))
print(add(-3, 10))
