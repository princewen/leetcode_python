"""

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

"""
"""用一个数组记录下每个数所需要的平方数的个数"""

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]
        for i in range(2, n + 1):
            t = 1
            minx = 0xffffffff
            while (i - t * t > 0):
                minx = min(minx, 1 + dp[i - t * t - 1])
                t = t + 1
            dp.append(minx if t * t > i else 1)
        return dp[n - 1]

