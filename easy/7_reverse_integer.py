"""

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

"""

"""my solution
每次除10 一般思路
要判断是否溢出
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        y = x if x > 0 else -x
        z = 0
        while y > 0:
            z = z * 10 + y % 10
            y /= 10
        z = z if x > 0 else -z
        if z > 0xffffffff or z < -0xffffffff:
            return 0
        else:
            return z

