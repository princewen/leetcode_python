"""

Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

"""
"""动态规划，现在是一个环，在上一题的基础上我们可以进行两轮的循环，比较两轮循环的最大者"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 4:
            return max(nums)
        else:
            first = second = 0
            for i in nums[1:]:
                first, second = second, max(second, first + i)
            max1 = second

            first = second = 0
            for i in nums[:-1]:
                first, second = second, max(second, first + i)
            return max(second, max1)

