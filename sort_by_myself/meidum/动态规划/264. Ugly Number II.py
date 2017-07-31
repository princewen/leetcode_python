"""

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

"""
"""
设置3个下标，对应2、3、5当前乘到的位置，随后计算下一个最小的ugly数，将其加入数组
"""
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            u2 , u3, u5 = 2 * ugly[i2],3 * ugly[i3] , 5 * ugly[i5]
            minu = min(u2,u3,u5)
            if minu == u2:
                i2 = i2 + 1
            if minu == u3:
                i3 = i3 + 1
            if minu == u5:
                i5 = i5 + 1
            ugly.append(minu)
        return ugly[-1]