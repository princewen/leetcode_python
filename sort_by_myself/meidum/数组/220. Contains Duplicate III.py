"""

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

"""
"""桶排序的思想，一个桶存储除差值相同以后结果的数，如果相邻k以内的两个数的结果落在同一个桶内，则返回True
如果落在相邻桶内，则判断二者的差的绝对值是否在允许差值以内
同时需要注意的是要保证桶只存储k个值
"""

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums) < 2 or t < 0:
            return False
        w = t + 1
        d = {}
        for i in range(len(nums)):
            m = nums[i] // w
            if m in d:
                return True
            elif (m - 1 in d) and abs(nums[i] - d[m - 1]) < w:
                return True
            elif (m + 1 in d) and abs(nums[i] - d[m + 1]) < w:
                return True
            else:
                d[m] = nums[i]
                if i >= k:
                    del d[nums[i - k] // w]
        return False

