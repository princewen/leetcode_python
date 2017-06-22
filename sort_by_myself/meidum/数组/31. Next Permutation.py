"""

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""

"""
https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
基本思想就是先找到从右往左的的最长递增序列，随后得到序列前面的一个数a，再从右开始找到第一个比a大的数b，交换ab，然后把a后面的序列进行reverse
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - 1
        while nums[right] <= nums[right - 1] and right - 1 >= 0:
            right = right - 1
        if right == 0:
            self.reverse(nums, 0, len(nums) - 1)
        else:
            pivot = right - 1
            successor = 0
            for i in range(len(nums) - 1, pivot, -1):
                if nums[i] > nums[pivot]:
                    successor = i
                    break
            nums[pivot], nums[successor] = nums[successor], nums[pivot]
            self.reverse(nums, right, len(nums) - 1)

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
