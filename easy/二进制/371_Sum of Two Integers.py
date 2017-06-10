"""

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.

"""

"""
思路：强大的位运算，不能用+ and -，考虑位运算，按位加
那么 1+1=10相当于 按位与再左移1位，1+0=1相当于按位异或，所以 按照这个思路进行迭代

"""
"""但是，这个对python不适用！，当输入负数时，会超时"""
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a==0:
            return b
        if b==0:
            return a
        while b:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a


"""python solution"""
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        """有疑问,python把有符号数当作无符号数处理"""
        return a if a <= MAX else ~(a ^ mask)