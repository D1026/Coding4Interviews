def getMin(array):
    # len(array) <= 1
    if not array:
        return None
    if len(array) == 1:
        return array[0]

    # 是否为单调不减数组（即旋转数组长度为0）,
    sorted = True
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            sorted = False
            break
    if sorted is True:
         return array[0]

    left = 0
    right = len(array) - 1
    mid = (left + right) // 2
    while True:
        # if array[mid] >= array[left] and array[mid] <= array[right]:
        #     return array[0]
        # 无法处理[1,1,1,0,1]，检查是否顺序 应该搜索到底，放在while True 外面

        if right == left + 1:
            return array[right]
        if array[mid] >= array[left]:
            left = mid
        else:
            right = mid
        mid = (left + right) // 2


print(getMin([4, 5, 6, 1, 2]))
print(getMin([5, 3, 4]))
print(getMin([7]))
print(getMin([1, 1, 1, 0, 1]))
