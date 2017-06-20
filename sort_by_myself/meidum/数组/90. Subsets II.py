"""

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""
"""这里要去重，所以之前的方法得到的数组首先要判断是否已经有了，判断是否存在首先需要对数组进行排序"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums)==0:
            return []
        if len(nums) == 1:
            return [[],[nums[0]]]
        for each in self.subsetsWithDup(nums[1:]):
            if sorted([]+each) not in res:
                res.append(sorted([]+each))
            if sorted([nums[0]] +each) not in res:
                res.append(sorted([nums[0]] + each))
        return res

"""if S[i] is same to S[i - 1], then it needn't to be added to all of the subset, just add it to the last l subsets which are created by adding S[i - 1]"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                l = len(res)
            for j in range(len(res)-l,len(res)):
                res.append(res[j]+[nums[i]])
        return res