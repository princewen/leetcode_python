"""

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:


"""
"""统计岸边的个数，很容易看出岸边数是元素为1的个数*4，减去相邻两个数都为1的邻居个数*2，那么我们在统计邻居的时候，为了避免重复，循环每一个元素时只统计其上方和左方是不是陆地"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num = 0
        neighbor = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num = num + 1
                    if i > 0 and grid[i-1][j] == 1:
                        neighbor += 1
                    if j>0 and grid[i][j-1] == 1:
                        neighbor += 1
        return num * 4 - neighbor *2