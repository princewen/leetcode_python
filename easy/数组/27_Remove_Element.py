"""

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.



"""

""" my solution 
借鉴26题的思路，直接遍历，由于前面的已经遍历过，可以直接替换掉元素的值
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index = index + 1

        return index


"""other solution
交换的思路
"""