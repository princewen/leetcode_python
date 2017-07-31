"""

Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1


"""
"""递归的思路"""


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n & 1 == 0:
            ret = ret + 1
            n = n >> 1
        if n == 1:
            return ret
        else:
            ret = ret + 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))
        return ret

"""找到规律，如果这个数比4大1或者等于3，减1，如果其他情况+1"""

class Solution(object):
    def integerReplacement(self, n):
        rtn = 0
        while n > 1:
            rtn += 1
            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return rtn