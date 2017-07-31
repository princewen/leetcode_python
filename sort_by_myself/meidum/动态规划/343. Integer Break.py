"""

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

"""

"""my solution 以此计算到达该数前每一个数能达到的最大值"""
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = [0] * n
        ret[0] = 1
        for i in range(2, n + 1):
            maxi = 0
            for t in range(1, i):
                maxi = max(maxi, max(ret[t - 1], t) * max(ret[i - t - 1], i - t))
            ret[i - 1] = maxi
        print(ret)
        return ret[-1]


