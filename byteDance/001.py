"""
P为给定的二维平面整数点集。定义 P 中某点x，如果x满足 P 中任意点都不在 x 的右上方区域内（横纵坐标都大于x），则称其为“最大的”。求出所有“最大的”点的集合。（所有点的横坐标和纵坐标都不重复, 坐标轴范围在[0, 1e9) 内）
如下图：实心点为满足条件的点的集合。请实现代码找到集合 P 中的所有 ”最大“ 点的集合并输出。

输入描述:

第一行输入点集的个数 N， 接下来 N 行，每行两个数字代表点的 X 轴和 Y 轴。
对于 50%的数据,  1 <= N <= 10000;
对于 100%的数据, 1 <= N <= 500000;

输出描述:

输出“最大的” 点集合， 按照 X 轴从小到大的方式输出，每行两个数字分别代表点的 X 轴和 Y轴。

输入例子1:

5
1 2
5 3
4 6
7 5
9 0

输出例子1:

4 6
7 5
9 0
"""
from numpy import array
detype = [('x', int), ('y', int)]
n = int(input())
points = array([(0, 0)]*n, dtype=detype)
for i in range(n):
    points[i] = eval(','.join(input().split()))

print(points)
print(type(points))

points.sort(order='x')
print(points)

maxes = []
for point in points:
    flag = 1
    for i in range(n):
        if points[i]['x'] > point['x'] and points[i]['y'] > point['y']:
            flag = 0
            break
    if flag:
       maxes.append(point)

for max in maxes:
    print(max[0], max[1])