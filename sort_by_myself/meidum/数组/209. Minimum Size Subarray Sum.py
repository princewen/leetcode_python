"""

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

"""

"""两个指针的思路，一个指针在前，一个指针在后"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = j = 0
        sums = 0
        minl = len(nums)+1
        while j<len(nums):
            sums = sums + nums[j]
            j = j + 1
            while sums >= s:
                minl = min(minl,j-i)
                sums = sums - nums[i]
                i = i + 1
        return minl if minl<=len(nums) else 0