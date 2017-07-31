"""

Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""

"""
构造两个数来模拟三进制，以其中一位来说：
两个数这一位的变化分分别是 0 1 0 0 和 0 0 1 0
那么对第一个数来说，新来一个1，如果第二个数是0，则它这一位变为1，否则变为0
对于第二个数来说，新来一个1，如果第一个数是1，则它变为0，如果第一个数为0，则原来是1变为0，原来是0变为1
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones