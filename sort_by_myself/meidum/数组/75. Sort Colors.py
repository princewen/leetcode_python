"""

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

"""
"""可以看到，这道题的做法非常巧妙，首先全都复值为2，小于2的j个值赋予1，等于0的i个值赋值0，那么也就是
（0，i）位置变为了0，（i，j）位置变为了1，后面的数变为了2"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j]=1
                j = j + 1
            if v==0:
                nums[i] = 0
                i = i + 1