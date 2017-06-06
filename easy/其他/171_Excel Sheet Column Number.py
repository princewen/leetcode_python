"""

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

"""

"""
my solution
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in s:
            count = count * 26 + (ord(i) - 65) % 26 + 1
        return count

"""other solution : 1 line"""

def titleToNumber(self, s):
    return reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,s))