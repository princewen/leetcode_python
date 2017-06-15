"""

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

"""

"""其实跟第一题是一样的题目"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = dict()
        for i in range(0,len(numbers)):
            sub = target - numbers[i]
            if sub in res.keys():
                return [res[sub]+1,i+1]
            else:
                res[numbers[i]] = i
        return []