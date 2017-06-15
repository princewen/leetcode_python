"""

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.


"""

"""my solution
先把不为零的往前放，最后补0
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        for i in range(index,len(nums)):
            nums[i] = 0