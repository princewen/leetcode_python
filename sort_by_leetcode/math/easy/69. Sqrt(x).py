"""

Implement int sqrt(int x).

Compute and return the square root of x.

"""
"""采用二分搜索的思路"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<=0:
            return 0
        else:
            left = 1
            right = x
            while left <= right:
                mid = (left+right) / 2
                a1 = mid*mid - x
                a2 = (mid-1)*(mid-1) -x
                if a1*a2 <= 0:
                    break
                elif a1 * a2 >0 and a1<0:
                    left = mid+1
                else:
                    right = mid-1
            if a1 == 0:
                return mid
            else:
                return mid-1