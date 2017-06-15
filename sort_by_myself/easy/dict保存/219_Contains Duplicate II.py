"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
只要有一组相同的数，他们的下表之差小于等于k，就返回True，题目理解有误，不过仍然使用字典保存结果

"""

"""这里要注意一个细节，判断value是否在res中时，如果时判断是否在res.keys()中，会超时"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        res = dict()
        for index, value in enumerate(nums):
            if value in res and index - res[value] <= k:
                return True
            res[value] = index
        return False