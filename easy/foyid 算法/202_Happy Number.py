"""

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1


"""


"""
solution 1: floyid 检测是否有环的算法，如果能到1，则fast先到1，随后等待slow得到1，如果不会得到1，则fast会追上slow
则此时存在圈，不会得到1
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n
        fast = sum([int(x) ** 2 for x in str(n)])
        while fast != slow:
            slow = sum([int(x) ** 2 for x in str(slow)])
            fast = sum([int(x) ** 2 for x in str(fast)])
            fast = sum([int(x) ** 2 for x in str(fast)])
        return slow == 1

"""
solution 2 : 使用一个set保存出现过的数字，如果某个数字已经在set中了，说明出现了环，判断此时的n是否为1即可
"""
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