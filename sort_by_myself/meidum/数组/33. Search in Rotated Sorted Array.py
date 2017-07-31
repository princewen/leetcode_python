"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.


"""
"""
仍然使用二分搜索的方法：
分三种情况：
1、mid的值与target相等，直接返回
2、nums[mid] 大于等于 nums[left] 说明这一段仍是有序递增的，所以如果target < nums[mid] 并且 target >= nums[left]则将right变为mid-1，否则
将left变为mid+1
3、nums[mid] 小于 nums[left] 说明这一段已经出现了分隔，再根据target的值进行判断。
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1




