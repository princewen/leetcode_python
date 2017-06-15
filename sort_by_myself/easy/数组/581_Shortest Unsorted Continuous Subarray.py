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
Subscribe to see which companies asked this question.

"""
"""将数组排序，并与原数组zip，然后判断每个元素是否相同，如果全是相同，则无需排序，返回0，否则，返回不相同的个数"""

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        is_same = [a == b for (a, b) in list(zip(nums, sorted(nums)))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)
