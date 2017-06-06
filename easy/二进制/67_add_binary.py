"""

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

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
