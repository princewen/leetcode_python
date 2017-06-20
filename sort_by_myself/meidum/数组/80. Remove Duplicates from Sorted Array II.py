"""

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

Subscribe to see which companies asked this question.

"""
"""我的思路是比较该数是否已经出现了两次"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 2:
            return len(nums)
        index = 2
        for num in nums[2:]:
            if num == nums[index-1] and num == nums[index-2]:
                continue
            else:
                nums[index] = num
                index = index + 1
        return index

"""更简单的思路是判断是否与倒数第二个相等"""
def removeDuplicates(self, nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    return i