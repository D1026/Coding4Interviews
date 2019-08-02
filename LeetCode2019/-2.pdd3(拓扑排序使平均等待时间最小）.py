def findOrder(self, numCourses: int, times: list[int], prerequisites: List[List[int]]) -> List[int]:
    edges = {i: [] for i in range(numCourses)}
    degrees = [0] * numCourses
    for i, j in prerequisites:
        edges[j].append(i)
        degrees[i] += 1
    que = []
    for i in range(numCourses):
        if degrees[i] == 0:
            que.append(i)
    res = []
    temp = []
    while que or temp:
        """
        当前入度为0的一批内按执行时间sort， 下一批（这一批全部执行完）入度为0一起sort. 未必是全局最优解，不能证明"""
        node = que.pop(0)
        res.append(node)
        for i in edges[node]:
            degrees[i] -= 1
            if degrees[i] == 0:
                temp.append(i)
        if not que:
            temp.sort(key=times.__getitem__)
            que.extend(temp)
            temp.clear()
    if len(res) == numCourses:
        return res
    else:
        return []

"""
弹出前，que按执行时间sort
"""


def findOrder(self, numCourses: int, times:list[int], prerequisites: List[List[int]]) -> List[int]:
    edges = {i: [] for i in range(numCourses)}
    degrees = [0] * numCourses
    for i, j in prerequisites:
        edges[j].append(i)
        degrees[i] += 1
    que = []
    for i in range(numCourses):
        if degrees[i] == 0:
            que.append(i)
    que.sort(key=times.__getitem__)
    res = []
    while que:
        node = que.pop(0)
        res.append(node)
        for i in edges[node]:
            degrees[i] -= 1
            if degrees[i] == 0:
                que.append(i)
        que.sort(key=times.__getitem__)
    if len(res) == numCourses:
        return res
    else:
        return []