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
# flag = [[False] * 3] * 4
# print(flag)
# i, j = 0, 0
# print(flag[i][j])
# flag[i][j] = True
# print(flag)
# # --- output:[[True, False, False], [True, False, False], [True, False, False], [True, False, False]]
# print(id(flag[0]))
# print(id(flag[1]))
# print(id(flag[0]) == id(flag[1]), id(flag[0]) == id(flag[2]))
# # 2364702089864
# # 2364702089864
# # True True
#
# a = [0]*4
# print(a)    # [0, 0, 0, 0]
# print(id(a[0]) == id(a[1]))    # True
# a[1] = 1
# print(id(a[0]) == id(a[1]))    # False
# print(a)    # [0, 1, 0, 0]
#
# b = [[4] * 4] * 3
# print(b, type(b))   # [[4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4]] <class 'list'>
# print(id(b[0]) == id(b[1]))    # True
# b[1][1] = 1
# print(id(b[0]) == id(b[1]))    # True
# print(b)    # [[4, 1, 4, 4], [4, 1, 4, 4], [4, 1, 4, 4]]

# def steps(n):
#     count = 0
#     if n == 1: return count
#     from math import sqrt
#     while n > 1:
#         temp = int(sqrt(n))
#         count += n - temp*temp
#         n = temp
#         count += 1
#     return count-1
# print(steps(27))

# -----
def times(s):
    if not s:
        return 0
    u, v = 5, 6
    t_move = 0
    t_pres = len(s)
    for i in range(len(s)//2):
        x = int(s[2*i])
        y = int(s[2*i+1])
        t1 = abs(max(x, y) - max(u, v))
        t2 = abs(min(x, y) - min(u, v))
        t_move += max(t1, t2)
        # if x in (u, v) and y in (u, v):
        #     t_pres += 2
        # elif x in (u, v) or y in (u, v):
        #     t_pres += 1
        # else:
        #     t_pres += 0
    if len(s)//2 != 0:
        last = int(s[-1])
        t_move += min(abs(last-u), abs(last-v))
        t_pres += 0 if last in (u, v) else 1

    return t_move+t_move

print(times('56'))


