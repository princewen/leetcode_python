"""

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

"""
"""这里用三个值记录前三大的数字，要注意是三个不同的数字，重复的数字不记录排序，所以要注意判断条件"""
"""这里用三个值记录前三大的数字，要注意是三个不同的数字，重复的数字不记录排序，所以要注意判断条件"""
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2= max3=None
        for num in nums:
            if num > max1:
                max2,max3 = max1,max2
                max1=num
            elif num > max2 and num < max1:
                max2,max3= num,max2
            elif num > max3 and num < max2:
                max3 = num
        return max1 if max3==None else max3