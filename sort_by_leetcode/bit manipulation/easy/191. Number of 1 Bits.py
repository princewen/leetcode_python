"""

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.



"""
"""
这里用到的二进制知识是：一个数与比自己小1的数按位与运算，会将自己所对应的二进制数的最后一个1变为0。
考虑如下的例子： 13的二进制数为1101，12的二进制数为1100
则 （1101）& （1100） --》（1100）
1100代表的数是10，9的二进制数为1001，则：
1100 & 1001 --》1000
依次类推
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n = n & (n-1)
            count = count + 1
        return count