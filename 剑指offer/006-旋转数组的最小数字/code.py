def minNumberInRotateArray(rotateArray):
    # write code here
    if not rotateArray:
        return 0
    low = 0
    high = len(rotateArray) - 1
    while True:
        mid = (low + high) // 2
        if rotateArray[mid] >= rotateArray[low]:
            low = mid
        else:
            high = mid
        if rotateArray[mid] < rotateArray[mid-1]:
            return rotateArray[mid]

print(minNumberInRotateArray([2, 3, 1]))
print(minNumberInRotateArray([1,1,1,0,1]))
print(minNumberInRotateArray([]))

# --- 原作者这个解法是错的，最后 left, mid, right 是三个相邻元素时，算法无限循环不会收敛 ---