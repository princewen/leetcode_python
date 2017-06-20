"""

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

"""

"""可以使用hash table保存下数组1的出现的元素，然后判断数组2中的各元素是否在数组1中出现过，但直接使用set更简单"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums1 = set(nums1)
        return [x for x in set(nums2) if x in nums1] 
