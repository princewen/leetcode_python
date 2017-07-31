"""

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

"""

"""分清楚多种情况"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[-1] > nums[0]:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif mid == len(nums) - 1:
                return nums[mid]
            elif nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            elif nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
