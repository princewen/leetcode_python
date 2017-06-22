"""

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

"""
"""直接使用数学公式即可:0的个数= n/5 + n/(5^2)+.......
"""
class Solution(object):
    def trailingZeroes(self, n):
        zeroCnt = 0
        while n > 0:
            n = n/ 5
            zeroCnt += n

        return zeroCnt