"""
Given an integer, write a function to determine if it is a power of two.
"""
"""考虑二进制的解法，对于2的倍数来说，它只有一位二进制位不为0，而相邻两个数的按位与有一个特点，就是把大数的最低一位1变为0，举个例子
3的二进制是 11，2的二进制是10，二者按位与是10，3的最后一位1变为了0
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and not (n & n-1)