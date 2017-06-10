"""

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""

"""my solution
从最后一位往前加，其实比较繁琐
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        extra = 0
        sum = ''
        for i in range(1,min(len(num1),len(num2))+1):
            sum = str((ord(num1[-i])+ord(num2[-i])-96+extra)%10)+sum
            extra = (ord(num1[-i])+ord(num2[-i])+extra-96)/10
        if len(num1) > i:
            for j in range(i+1,len(num1)+1):
                sum = str((ord(num1[-j])-48+extra)%10)+sum
                extra = (ord(num1[-j])+extra-48)/10
        if len(num2) > i:
            for j in range(i+1,len(num2)+1):
                sum = str((ord(num2[-j])-48+extra)%10)+sum
                extra = (ord(num2[-j])+extra-48)/10
        if extra>0:
            sum = str(extra)+sum
        return sum