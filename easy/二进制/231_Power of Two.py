"""

Given an integer, write a function to determine if it is a power of two.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

"""
"""
判断一个数是否是2的此方数，只需判断是否只有1位二进制位是1即可，用之前提到的方法，n与n-1的按位与可以把最右边一位1变为0。
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and not (n & n-1)