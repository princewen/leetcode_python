"""
判断是不是一个回文数

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

Subscribe to see which companies asked this question.

"""

"""solution
先得到x是几位数，如五位数得到render=10000
然后分别判断最左边一位和最右边一位是否相等
同时x去掉左右一位，先对render取余再除以10，而render则缩小100倍
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        render = 1
        while x / render >= 10:
            render *= 10

        while x:
            left = x / render
            right = x % 10
            if left != right:
                return False

            x = (x % render) / 10
            render /= 100

        return True
