"""

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

"""先对数组排序，然后进行遍历，采用类似二分搜索的思想，用两个指针，这样时间复杂度是O（n^2)"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                m = nums[i]+nums[l]+nums[r]
                if m<0:
                    l = l + 1
                elif m>0:
                    r = r - 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l = l+1
                    while l<r and nums[r] == nums[r-1]:
                        r = r -1
                    l = l + 1
                    r = r - 1
        return res