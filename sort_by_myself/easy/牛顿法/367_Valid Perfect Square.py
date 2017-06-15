"""

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False

"""

"""my solution
二分搜索的方法
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        left = 0
        right = num
        while left <= right:
            mid = (right-left)/2+left
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

"""other solution
使用牛顿方法解:http://blog.csdn.net/hyc__/article/details/41117009
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while r*r > num:
            r = (r + num/r) / 2
        return r*r == num

