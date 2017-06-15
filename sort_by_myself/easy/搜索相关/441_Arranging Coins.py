"""

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

"""

"""binary search"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        left = 1
        right = n/2
        while left <= right:
            mid = (right-left)/2+left
            total = (mid * (mid+1)) / 2
            if total > n:
                right = mid - 1
            elif n - total < mid + 1:
                return mid
            elif n-total == mid + 1:
                return mid+1
            else:
                left = left + 1
        return left