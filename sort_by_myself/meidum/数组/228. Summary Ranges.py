"""

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

"""

"""
我的思路：很简单的遍历数组，判断前一个是否比后一个小1，要注意将最后的部分补上

"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        index = 0
        res = []
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                continue
            else:
                if i-1 == index:
                    res.append(str(nums[index]))
                else:
                    res.append(str(nums[index])+'->'+str(nums[i-1]))
                index = i
        if index == len(nums)-1:
            res.append(str(nums[index]))
        else:
            res.append(str(nums[index])+'->'+str(nums[-1]))
        return res


"""其他的解法，保存range于一个数组中，加一个逗号的原因是将后面添加的变成一个iterable的对象，即[],相当于[[]] """
class Solution(object):
    def summaryRanges(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]


