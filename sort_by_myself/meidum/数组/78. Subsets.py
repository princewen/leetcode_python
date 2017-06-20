"""

Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""
"""my solution 递归的方法，每次递归从1到最后一个元素，直到只有一个元素"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums:
            return []
        if len(nums) == 1:
            return [[],[nums[0]]]
        for each in self.subsets(nums[1:]):
            res.append([]+each)
            res.append([nums[0]] + each)
        return res