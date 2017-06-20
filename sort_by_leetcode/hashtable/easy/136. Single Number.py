"""

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""
"""这道题虽然放在了hashtable里，但其实用二进制的算法更容易求解
两个相同数的二进制异或为0，所以遍历一边数组，出现两次的异或值变为0，那么剩下的数就是出现一次的数
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res = res ^ i
        return res