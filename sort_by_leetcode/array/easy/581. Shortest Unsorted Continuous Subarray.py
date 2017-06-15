"""

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

"""

"""all_same[::-1]返回的不是从正向数的索引，返回的是以最后一个元素为0索引，倒数第二个元素为1索引的反向数列的索引值"""
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_same = [a == b for (a, b) in zip(nums, sorted(nums))]
        return 0 if all(all_same) else len(nums) - all_same.index(False) - all_same[::-1].index(False)
