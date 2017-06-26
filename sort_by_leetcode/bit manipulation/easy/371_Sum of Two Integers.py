"""

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.

"""

"""
思路：强大的位运算，不能用+ and -，考虑位运算，按位加
如果两位都是0，则取0，如果两位中有一位是1，则是1，如果两位都是1，则是10，那么我们可以用异或来表示这种关系，但是两个都是1的情况下，还需要在前一位补一个1，所以再用按位与并移1位来表示需要补上的一个1
例如考虑四位二进制位的3（0011）和 5（0101）相加：
第一轮
a = 0011 ^ 0101 = 0110
b = 0011 & 0101 = 0001 << 1 = 0010
第二轮:
a = 0110 ^ 0010 = 0100
b = 0110 & 0010 = 0010 << 1 = 0100
第三轮：
a = 0100 ^ 0100 = 0000
b = 0100 & 0100 = 0100 << 1 = 1000
最后一轮：
a = 0000 ^ 1000 = 1000
b = 0000 & 1000 = 0000迭代终止，返回a

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