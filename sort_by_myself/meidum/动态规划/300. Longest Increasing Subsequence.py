"""

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

"""
"""O（n2）的动态规划，依次计算每个位置的最长递减序列"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1]
        maxL = 1
        # 这样写index不是数组的原index，而是从0开始，所以不对！
        # for index,value in enumerate(nums[1:]):
        for i in range(1, len(nums)):
            maxI = 1
            for index, value in enumerate(nums[:i]):
                if value < nums[i]:
                    maxI = max(maxI, dp[index] + 1)
            dp.append(maxI)
            maxL = max(maxL, maxI)
        return maxL


"""O(nlogn)的策略：耐心排序法
https://segmentfault.com/a/1190000003819886
"""

def lengthOfLIS(self, nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) / 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        #说明前面有i个比他小的
        size = max(i + 1, size)
    return size