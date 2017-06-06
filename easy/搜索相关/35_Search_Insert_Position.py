"""

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

"""

"""
my solution
类似于二分搜索，注意结束的条件，如果结束循环的条件少了等号，容易漏掉情况
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left


"""other solution
类似于二分搜索"""

class Solution(object):
    def searchInsert(self, nums, key):
        if key > nums[len(nums) - 1]:
            return len(nums)

        if key < nums[0]:
            return 0

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)/2
            if nums[m] > key:
                r = m - 1
                if r >= 0:
                    if nums[r] < key:
                        return r + 1
                else:
                    return 0

            elif nums[m] < key:
                l = m + 1
                if l < len(nums):
                    if nums[l] > key:
                        return l
                else:
                    return len(nums)
            else:
                return m