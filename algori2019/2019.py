# --- bD 01 ---
"""
第一年出生一头牛，
每头牛在 3~7岁（第3~7年）每年会生一头牛，10岁之后死亡（10岁活着），
--就是说，每头牛都会在他（出生那一年算作第一年）的 第三年 到 第七年 每年 生一头 小牛，第 11 年死亡
求 n 年牛数
"""
# n = int(input())
# if n < 3:
#     print(1)
# else:
#     base = [0, 1]
#     for i in range(n-1):
#         base.append(base[-1]+base[-2])
#     if n <= 7:
#         print(base[n])
#     else:
#         die = [0]*10 + base[:-10]
#         no_born = [0]*7 + base[:-7]
#         # die_sum = 2*die[n]+die[n-1] - 1
#         no_born_sum = 2*no_born[n]+no_born[n-1] - 1
#         print(base[n]-die[n]-no_born_sum)

# --- bD 02 ---
"""
1~9 x 4 共36张牌，你手里13张，求出再给你一张什么牌，能和牌（求所有解，从小到大输出）
和牌条件：1、两张 数字一样的牌是 雀头
          2、剩下12张 是顺子或者刻子：顺子如123，456，刻子如：111,444
"""
# s = input().split()
# cards = []
# for i in s:
#     cards.append(int(i))
# cards.sort()
#
# shun = []
# ke = []
# for i in range(1, 10):
#     shun.append([i]*3)
#     if i <= 7:
#         ke.append([i, i+1, i+2])
# sk = shun + ke
#
# # --- can't deal with...
# print(7)

# --- bD 03 ---
"""
输入 n, d；输入数轴上 n 个点（每个点都是整数），找出 这样3个点：其中任意两点最大距离 < d；
给出解的个数
（点都是整数）
"""
n, d = eval(','.join(input().split()))
p = input().split()
ps = []
for i in p:
    ps.append(int(i))

flag = [0]*(n-2)
for i in range(n-2):
    if (ps[i+2] - ps[i]) > d:
        flag[i] = 1

count = 0
for i in flag:
    count = count + i
if count == n-2:
    print(0)
    exit()

# --- ---
else:
    print(n-2-count)

# --- bD 04 ---
"""1, 0, 0, 1, 1, 1, 0, 1
    n 个数， 可以有k次机会 把 1 变 0，
    变化后最长全 1 子序列长度
"""


# --- dW ---
"""
四支球队 A B C D, 踢小组赛（每支球队都要跟 其他三支球队踢一场，共 3+2+1=6 场），
每场比赛 胜者得 3 分，负者得 0 分，平局则双方各得 1 分，
输出：小组赛 比赛结果 的所有 可能得分情况，（不区别球队，只求得分 不同组合的数目，例如 9 4 4 1 与 1 4 4 9视为一种情况）
"""