"""

Determine whether an integer is a palindrome. Do this without extra space.

"""
"""
1、如果是负数，直接返回False
2、首先得到这个数的位数count，如果是432，我们就得到100
3、然后用x余10得到最右边一位数，用x除count得到最左边一位数
4、去掉x的左右各一位，count除以100，循环直到x为0
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        count = 1
        while x / count >= 10:
            count = count * 10
        while x:
            left = x % 10
            right = x / count
            if left != right:
                return False
            x = (x % count) / 10
            count = count / 100
        return True
