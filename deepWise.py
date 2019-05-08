# 4支球队 a, b, ,c, d
# 思路：递归枚举，a 与其他球队，的情况枚举完成之后，则只剩下 b c d之间的情况，4 x 4得分矩阵退化为 3 x 3 ...
# score[i][j] score[j][i] 为相互确定关系 3-0 0-3 1-1
import numpy as np

score = np.array([-1]*16, dtype=int).reshape([4, 4])
print(len(score))

for i in range(4):
    score[i][i] = 0

s = [3, 1, 0]

def get(x):
    if len(x) == 1:
        print(np.sum(score, axis=0))
        return

    x[0][1] = 3
    # ...
    # get(x[1:][1:])
    x[0][1] = 1
    # ...
    x[0][1] = 0
    # ...
