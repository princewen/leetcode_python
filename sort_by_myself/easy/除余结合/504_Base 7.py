"""

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].

"""

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        abs_num = abs(num)
        res=''
        while abs_num!=0:
            res=str(abs_num%7)+res
            abs_num=abs_num/7
        return res if num>=0 else '-'+res