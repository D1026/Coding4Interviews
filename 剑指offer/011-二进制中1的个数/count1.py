n = -1
s = n & (n-1)
print(bin(n))
print(bin(n-1))
print(bin(s))
print(bin(n ^ (n-1)))
# --- output ---
# -0b1
# -0b10
# -0b10

from ctypes import *

def countOf1(x):
    count = 0
    while c_int(x).value:
    # while x:
    #     print(c_int(x).value)
    #     print('x= ', x)    # x=  -426961504325626845386774724...
        x = x & (x-1)
        count = count + 1
    return count

print(countOf1(-3))

# x = -7
# count = 0
# while x:
#     if c_int(x).value != x:
#         print('c_int---', c_int(x).value)
#         print('x= ', x)
#     count += 1
#     print('while: ', count)
#     x = x & (x - 1)