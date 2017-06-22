"""

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

"""

"""
采用递归的思路，从末位开始相加，要分五种情况进行讨论
1、a为空，返回b
2、b为空，返回a
3、a和b的末位都是1，递归的同时，末位添0，同时前面要再和'1'想加
4、a和b的末位都是0，递归的同时，末位添0
5、a和b的末位有一个为1，递归的同时，末位添1
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == '':
            return b
        if b == '':
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'
