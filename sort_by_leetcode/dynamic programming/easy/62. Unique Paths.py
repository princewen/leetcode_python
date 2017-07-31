"""

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?




"""

"""利用数学方法"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > n:
            m, n = m - 1, n - 1
        else:
            m, n = n - 1, m - 1
        if m <= 0 or n <= 0:
            return 1
        t = m + n
        sub = 1
        for i in range(1, n):
            t = t * (m + n - i)
            sub = sub * (i + 1)

        return t / sub

"""利用动态规划的方法"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = [[0 for t in range(n)] for x in range(m)]
        count[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    count[i][j] = 1
                elif i == 0:
                    count[i][j] = count[i][j - 1]
                elif j == 0:
                    count[i][j] = count[i - 1][j]
                else:
                    count[i][j] = count[i - 1][j] + count[i][j - 1]
        return count[m - 1][n - 1]



