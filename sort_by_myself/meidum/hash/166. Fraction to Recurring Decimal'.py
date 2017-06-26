"""


Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
Credits:
Special thanks to @Shangrila for adding this problem and creating all test cases.
"""
"""
1、判断两个数中有几个是负数
2、将两个数都变成绝对值之后在进行运算
3、先判断是否在字典中，再进行运算，否则会漏掉第一位
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'
        res = '-' if (numerator > 0) ^ (denominator > 0) else ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        res = res + str(numerator / denominator)
        remain = numerator % denominator

        if remain == 0:
            return res
        res = res + '.'
        dic = dict()
        while remain != 0:

            if remain in dic:
                res = res[:dic[remain]] + '(' + res[dic[remain]:] + ')'
                return res
            else:
                dic[remain] = len(res)

            onecode = remain * 10 / denominator
            remain = remain * 10 % denominator
            res = res + str(onecode)
        return res





