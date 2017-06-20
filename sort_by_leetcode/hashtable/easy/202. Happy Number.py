"""

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Credits:
Special thanks to @mithmatt and @ts for adding this problem and creating all test cases.

"""

"""解法1，用列表保存出现过的数，当出现重复的数字的时候，说明出现了循环，循环有两种情况，一种不是hayyp数，循环的数必不是1，如果是happy数，那么会出现1的不断循环"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        c = set()
        while not n in c:
            c.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
        return n==1

"""解法2，使用追赶法，快的指针每次前进两步，慢的指针每次只前进一步，当快的指针追上慢的指针即二者数字相同时，同样说明出现了
循环，情况同上"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n
        quick = sum([int(x) ** 2 for x in str(n)])
        while quick != slow:
            quick = sum([int(x) ** 2 for x in str(quick)])
            quick = sum([int(x) ** 2 for x in str(quick)])
            slow = sum([int(x) ** 2 for x in str(slow)])
        return slow == 1