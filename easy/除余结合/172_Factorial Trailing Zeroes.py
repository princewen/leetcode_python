"""

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

"""


class Solution(object):
    def trailingZeroes(self, n):
        zeroCnt = 0
        while n > 0:
            n = n / 5;
            zeroCnt += n

        return zeroCnt