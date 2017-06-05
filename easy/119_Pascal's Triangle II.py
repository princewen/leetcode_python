"""

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

"""

"""my solution
这里要提醒一下map函数的应用，map在python2中返回的是一个list，而在python3中返回的是一个map object，必须加一个list来进行类型转换
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(1,rowIndex+1):
            res = list(map(lambda x,y:x+y,res+[0],[0]+res))
        return res

"""other solution
非常类似
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row