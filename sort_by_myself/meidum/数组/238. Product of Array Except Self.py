"""

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

"""

"""
巧妙的思路，首先正向遍历数组，得到一个新数组，新数组中的第i个元素是原数组前i-1个元素的乘积
随后反向遍历数组，给新数组的每一个元素再乘上原数组后面的元素
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        output = []
        for i in range(len(nums)):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output