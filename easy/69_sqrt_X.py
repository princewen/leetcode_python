"""

Implement int sqrt(int x).

Compute and return the square root of x.


"""

"""my solution

基本上属于分治算法，二分搜索

"""


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

"""other solution"""
# Binary search
def mySqrt(self, x):
    l, r = 0, x
    while l <= r:
        mid = l + (r-l)//2
        if mid * mid <= x < (mid+1)*(mid+1):
            return mid
        elif x < mid * mid:
            r = mid
        else:
            l = mid + 1