"""

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

Subscribe to see which companies asked this question.

"""
""" 遍历数组，要考虑负数的情况以及0的情况，所以需要设置两个指针，如果前一步的最大值乘以了一个负数，会变成最小值，如果最小值乘上一个负数会变成最大值"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSoFar = nums[0]
        maxherepre = nums[0]
        minherepre = nums[0]
        maxhere = 0
        minhere = 0
        for num in nums[1:]:
            maxhere = max(max(maxherepre*num,minherepre*num),num)
            minhere = min(min(maxherepre*num,minherepre*num),num)
            maxSoFar=max(maxSoFar,maxhere)
            maxherepre = maxhere
            minherepre = minhere
        return maxSoFar