import numpy as np
def clockTrav(x):
    res = []
    x = np.array(x)
    # walked = [[False] * x.shape[1]] * x.shape[0]
    walked = np.zeros(x.shape)
    print(x)
    i, j = 0, 0
    direct = 0  # 0-向右，1-向下，2向左， 3-向上

    while not walked[i][j]:

        res.append(x[i][j])
        walked[i][j] = 1
        # print('visited:', (i, j), 'direct:', direct)
        if direct == 0:
            if j < x.shape[1]-1 and not walked[i][j+1]:
                j += 1
            else:
                print('flag')
                direct = 1
        if direct == 1:

            if i < x.shape[0]-1 and not walked[i+1][j]:
                print('visit [1, 2]')
                i += 1
            else:
                direct = 2
        if direct == 2:
            if j > 0 and not walked[i][j-1]:
                j -= 1
            else:
                print('flag2')
                direct = 3
        if direct == 3:
            if i > 0 and walked[i-1][j]:
                i -= 1
            else:
                print('flag3')
                direct = 0
    print('end:', direct)
    return res

print(clockTrav([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(clockTrav([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]))