"""

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

"""
my solution 用split分割字符串，然后找到长度最大的
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [str(x) for x in nums]
        return max([len(x) for x in ''.join(nums).split('0')])


"""
其他解法：遍历数组
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        ans = 0
        for num in nums:
            if num == 1:
                cnt = cnt + 1
                ans = max(ans,cnt)
            else:
                cnt = 0
        return ans