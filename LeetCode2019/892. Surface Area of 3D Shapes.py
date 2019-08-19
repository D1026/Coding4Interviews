"""
Easy

On a N * N grid, we place some 1 * 1 * 1 cubes.
Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
Return the total surface area of the resulting shapes.

Example 1:
Input: [[2]]
Output: 10
Example 2:
Input: [[1,2],[3,4]]
Output: 34
Example 3:
Input: [[1,0],[0,2]]
Output: 16
Example 4:
Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:
Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46

Note:
1 <= N <= 50
0 <= grid[i][j] <= 50
"""


class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        surface = adj = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    surface += grid[i][j] * 6 - (grid[i][j] - 1) * 2
                    if i < len(grid) - 1 and grid[i + 1][j]:
                        if grid[i + 1][j] >= grid[i][j]:
                            adj += grid[i][j]
                        else:
                            adj += grid[i + 1][j]
                    if j < len(grid[0]) - 1 and grid[i][j + 1]:
                        if grid[i][j + 1] >= grid[i][j]:
                            adj += grid[i][j]
                        else:
                            adj += grid[i][j + 1]

        return surface - adj * 2