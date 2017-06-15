"""

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

"""
"""利用118题的思路轻松求解"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(1, rowIndex + 1):
            res = list(map(lambda x, y: x + y, res + [0], [0] + res))
        return res
