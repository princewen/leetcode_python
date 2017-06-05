"""

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.


"""
"""my solution
最后一位与1进行按位与运算
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += (n & 1)
            n = n>>1
        return count

"""other solution
n&n-1的妙用，
n&(n-1)作用：将n的二进制表示中的最低位为1的改为0
n = 10100(二进制），则(n-1) = 10011 ==》n&(n-1) = 10000
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += 1
            n = (n & (n - 1))
        return count


