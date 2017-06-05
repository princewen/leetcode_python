"""

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 


"""
"""
my solution，这里要注意，不能直接除或者余26，首先要减一，举个例子就可以知道
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            res = chr((n - 1) % 26 + 65) + res
            n = (n - 1) / 26
        return res
