n = -1
s = n & (n-1)
print(bin(n))
print(bin(n-1))
print(bin(s))
# --- output ---
# -0b1
# -0b10
# -0b10
# python对二进制的表示与运算进行了封装
from ctypes import *

def countOf1(x):
    count = 0
    while c_int(x).value:
        print(c_int(x).value)
        x = x & (x-1)
        print(c_int(x).value)
        count = count + 1
    return count

print(countOf1(-3))