"""

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

"""

"""循环一遍数组，判断当前所能到达的最大位置，不需要判断最后一位数字
终止条件是，当遇到一个0的数时，当前所能到的最大位置小于等于该数的索引，不能继续前进
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        maxreach = 0
        for index, num in enumerate(nums[:-1]):
            if num == 0 and maxreach <= index:
                return False
            maxreach = max(maxreach, index + num)
        return maxreach >= len(nums) - 1
