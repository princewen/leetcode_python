"""

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

"""

"""
my solution ：使用一个字典
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = dict()
        for i in nums:
            if i in res.keys():
                res[i] = res[i]+1
            else:
                res[i] = 1
            if res[i] > len(nums)/2:
                return i


"""other solution
常数级的空间复杂度，因为最多的元素超过一半，所以该元素的count值减去其他所有元素的count值一定大于0，所以最后的cand一定是出现次数最多的元素
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cand = nums[0]
        count = 1
        for i in nums[1:]:
            if count == 0:
                cand,count = i,1
            else:
                if i == cand:
                    count = count + 1
                else:
                    count = count - 1
        return cand
