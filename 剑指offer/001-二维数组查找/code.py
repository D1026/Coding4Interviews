
def find(array, tar):
    row = len(array)
    col = len(array[0])
    i, j = 0, col-1
    while i < row and j >= 0:
        if array[i][j] < tar:
            i += 1
        else:
            if array[i][j] > tar:
                j -= 1
                i = 0
            else:
                return (i, j)
    return (-1, -1)

print(find([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]], 0))