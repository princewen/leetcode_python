"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

"""my solution
首先创建一个字典，用于保存已经遍历过的元素以及他们在字典中的位置
如果差值在字典中，则返回字典中的索引值以及该元素的索引值
如果差值不再字典中，将该元素加入字典
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = dict()
        for index, value in enumerate(nums):
            sub = target - value
            if sub in num_dict.keys():
                return [num_dict[sub], index]
            else:
                num_dict[value] = index

        return []


"""标准答案1
跟我的思路差不多，是把差值存入字典中
而且考虑了nums长度小于1的情况
"""


def twoSum(self, nums, target):
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[target - nums[i]] = i