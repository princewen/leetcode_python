"""

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
Subscribe to see which companies asked this question.

"""
"""傻傻的使用循环的方式生成杨辉三角，其实有更简单的方法：
注意判断输入为0行的情况
    1 3 3 1 0 
 +  0 1 3 3 1
 =  1 4 6 4 1
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:return []
        res = [[1]]
        for i in range(1,numRows):
            res.append(map(lambda x,y:x+y,res[-1]+[0],[0]+res[-1]))
        return res

