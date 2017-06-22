"""

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""

"""递归的进行调用，如果到N=2，则设置两个指针进行搜索，否则的话，进行递归"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def findNsum(nums, target, N, result, results):
            if N < 2 or len(nums) < N or target < nums[0] * N or target > nums[-1] * N:
                return
            if N == 2:
                l = 0
                r = len(nums) - 1
                while l < r:
                    sum = nums[l] + nums[r]
                    if sum == target:
                        results.append(result + [nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l = l + 1
                        l = l + 1
                        while l < r and nums[r] == nums[r - 1]:
                            r = r - 1
                        r = r - 1
                    elif sum < target:
                        l = l + 1
                    else:
                        r = r - 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                        findNsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results