"""

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

"""
"""首先第一次循环得到哪几行哪几列需要变0，同时记录首行首列要不要变0
然后第二次循环把除首行首列外变0，最后把首行首列变0
这样空间复杂度比较低
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        fr = False
        fc = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    if i == 0:fr = True
                    if j == 0:fc = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j]=0
        if fr:
            for t in range(len(matrix[0])):
                matrix[0][t] = 0
        if fc:
            for t in range(len(matrix)):
                matrix[t][0] = 0