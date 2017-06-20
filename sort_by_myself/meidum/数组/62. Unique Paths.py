"""

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

"""

"""my solution看作一个排列组合题，但要注意当只有一行或者一列时，只能有一个路线"""


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
