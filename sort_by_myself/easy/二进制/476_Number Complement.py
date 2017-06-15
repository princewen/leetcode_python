"""

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.


"""
"""与1进行按位与运算，保存每一位，存入stack中，随后转换为十进制"""
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        stack = []
        while num > 0:
            stack.append(1-(num & 1))
            num = num >> 1
        for i in range(len(stack)-1,-1,-1):
            res = res * 2 + stack[i]
        return res

"""更巧妙的方法，要得到对位取反，其实就是用全1的数字进行按位异或，但是要位数刚刚好"""
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i=1
        while i<=num:
            i = i << 1
        return (i-1) ^ num