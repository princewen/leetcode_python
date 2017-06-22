"""

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

"""
"""使用摩尔投票算法，设置两个count，注意到减的次数不到1／3，可以确保剩下的两个candidate是我们想要的"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        count1,count2,candidate1,candidate2=0,0,0,1
        for n in nums:
            if n == candidate1:
                count1 = count1 + 1
            elif n == candidate2:
                count2 = count2 + 1
            elif count1==0:
                count1,candidate1 = 1,n
            elif count2 == 0:
                count2,candidate2 = 1,n
            else:
                count1,count2 = count1-1,count2-1
        return [n for n in [candidate1,candidate2] if nums.count(n) > len(nums) //3]