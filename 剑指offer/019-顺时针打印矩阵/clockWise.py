def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    rst = []
    while right > left and bottom > top:
        for col in range(left, right + 1, 1):
            rst.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1, 1):
            rst.append(matrix[row][right])
        right -= 1
        for col in range(right, left - 1, -1):
            rst.append(matrix[bottom][col])
        bottom -= 1
        for row in range(bottom, top - 1, -1):
            rst.append(matrix[row][left])
        left += 1
    if right == left:
        for row in range(top, bottom + 1, 1):
            rst.append(matrix[row][right])
    elif top == bottom:
        for col in range(left, right + 1, 1):
            rst.append(matrix[top][col])

    return rst

print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiralOrder([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]))