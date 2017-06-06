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

"""

"""my solution
暴力循环
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            rows = [[1],[1,1]]
            for i in range(3,numRows+1):
                singlerow = []
                for j in range(i):
                    if j == 0 or j == i-1:
                        singlerow.append(1)
                    else:
                        singlerow.append(rows[i-2][j-1]+rows[i-2][j])
                rows.append(singlerow)
            return rows

"""other solution
为什么append不行
"""


def generate(self, numRows):
    res = [[1]]
    for i in range(1, numRows):
        res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]
    return res[:numRows]