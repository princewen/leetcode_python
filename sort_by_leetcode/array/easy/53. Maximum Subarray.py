"""

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

Subscribe to see which companies asked this question.

"""

"""要点：两个指针，一个指针记录当前的最大值a1，一个记录循环每个元素时的最大值a2
a2的更新规则是，如果a2+当前元素比原来a2大，则更新a2=原a2+当前元素，否则a2=当前元素
a1的更新规则是 a1 = a1 if a1 >a2 else a2
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum=maxSum=nums[0]
        for i in range(1,len(nums)):
            curSum = max(nums[i],curSum+nums[i])
            maxSum = max(curSum,maxSum)
        return maxSum