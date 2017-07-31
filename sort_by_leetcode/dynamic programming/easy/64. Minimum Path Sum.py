"""

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

"""
"""仍然是和62题一样的思路"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                if j == len(grid[0])-1 and i== len(grid)-1:
                    continue
                elif j == len(grid[0])-1:
                    grid[i][j] = grid[i+1][j] + grid[i][j]
                elif i == len(grid)-1:
                    grid[i][j] = grid[i][j] + grid[i][j+1]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i+1][j],grid[i][j+1])
        return grid[0][0]