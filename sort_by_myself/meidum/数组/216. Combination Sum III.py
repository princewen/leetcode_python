"""

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

"""

""" 递归求解"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        sub_res = self.combineStart(1, k, n)
        res += [x for x in sub_res if len(x) == k]
        return res

    def combineStart(self, start, k, n):
        print(start, k, n)
        if n <= 0:
            return []
        if k == 1:
            if n >= start and n < 10:
                return [[n]]
            else:
                return []
        res = []
        for i in range(start, 10):
            sub_res = self.combineStart(i + 1, k - 1, n - i)
            res += [[i] + x for x in sub_res]
        return res




