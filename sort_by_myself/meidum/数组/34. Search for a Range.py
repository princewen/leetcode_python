"""

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

"""
"""两次二分搜索，第一次用于得到范围的下界，第二次得到范围的上界，第二次的时候注意计算mid要加上1，否则，left的值有可能一直不变，导致mid一直不变"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        res = [-1, -1]
        if not nums:
            return res
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right - left) / 2 + left
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            res[0] = left
        else:
            return res
        right = len(nums) - 1
        while left < right:
            mid = (right - left) / 2 + left + 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        res[1] = right
        return res
