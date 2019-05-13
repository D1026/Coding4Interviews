# a = 'jasdyegfihaewgoi'
# for i in a:
#     i = 'A'
# print(a)
# # jasdyegfihaewgoi
# print(len(a))
# # 16
# # for i in iter， 'i' is a copy
#
# # --- 003 ---
# a = ['qw', 1, 4]
# print(a.pop())
# print(a)
#
# a = 1
# while a:
#     print('AAA')
#     break

# --- 5.13 ---
def exch(x):
    x[0], x[-1] = x[-1], x[0]

import numpy as np
a = np.arange(10)
print(a)
x = a[:3]
print(x)
exch(x)
print(x)
print(a)

