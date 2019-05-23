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
# def exch(x):
#     x[0], x[-1] = x[-1], x[0]
#
# import numpy as np
# a = np.arange(10)
# print(a)
# x = a[:3]
# print(x)
# exch(x)
# print(x)
# print(a)


# --- 关于 [] * int 扩展 ---
flag = [[False] * 3] * 4
print(flag)
i, j = 0, 0
print(flag[i][j])
flag[i][j] = True
print(flag)
# --- output:[[True, False, False], [True, False, False], [True, False, False], [True, False, False]]
print(id(flag[0]))
print(id(flag[1]))
print(id(flag[0]) == id(flag[1]), id(flag[0]) == id(flag[2]))
# 2364702089864
# 2364702089864
# True True

a = [0]*4
print(a)    # [0, 0, 0, 0]
print(id(a[0]) == id(a[1]))    # True
a[1] = 1
print(id(a[0]) == id(a[1]))    # False
print(a)    # [0, 1, 0, 0]

b = [[4] * 4] * 3
print(b, type(b))   # [[4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4]] <class 'list'>
print(id(b[0]) == id(b[1]))    # True
b[1][1] = 1
print(id(b[0]) == id(b[1]))    # True
print(b)    # [[4, 1, 4, 4], [4, 1, 4, 4], [4, 1, 4, 4]]
