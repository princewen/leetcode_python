"""

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

"""


"""
这里用到的方法是经典的除余相结合，得到一个数的最后一位简单的方法就是余10，得到这个数的除最后一位之外的n-1位，简单的方法就是除10
这里要注意的地方就是负数首先要先得到它的相反数在进行操作，最后再变为负数
这个题还有一个注意的地方就是别的语言如c++，java中整数有溢出，而python的整数是没有溢出的，所以我们最好手动判断是否溢出
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = x if x > 0 else -x
        res = 0
        while n:
            res = res * 10 + n % 10
            n = n / 10
        if res > 0x7fffffff:
            return 0
        return res if x > 0 else -res