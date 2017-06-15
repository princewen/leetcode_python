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

"""
solution：使用三个变量记录当前数组中最大的三个值，遍历数组
"""
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2 = max3 = None
        for num in nums:
            if num==max1 or num==max2 or num==max3:
                continue
            elif max1==None or num>max1:
                max3=max2
                max2=max1
                max1=num
            elif max2==None or num>max2:
                max3=max2
                max2=num
            elif max3==None or num>max3:
                max3=num
        return max3 if max3!=None else max1