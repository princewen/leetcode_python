"""

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""

"""
my solution : 超过时间限制，而且使用了额外的字典空间
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = dict()
        for i in nums:
            if i in res.keys():
                res[i] = res[i] + 1
            else:
                res[i] = 1
            if res[i] > 1:
                del res[i]

        return res.keys()[0]

"""正确解法：使用异或位运算，两个相同的数的位运算结果为0，那么剩下的数肯定就是那个单一的数"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        return res
