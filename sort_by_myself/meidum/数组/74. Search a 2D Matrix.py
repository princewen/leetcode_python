"""

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

"""
"""my solution 相当于两次二分搜索"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        left = 0
        right = len(matrix) - 1
        rowlen = len(matrix[0]) - 1
        row = 0
        if matrix[right][rowlen] < target or matrix[0][0] > target:
            return False
        while left <= right:
            mid = (right - left) / 2 + left
            if matrix[mid][0] <= target and matrix[mid][rowlen] >= target:
                row = mid
                break
            elif matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][rowlen] < target:
                left = mid + 1
        left = 0
        right = rowlen
        while left <= right:
            mid = (right - left) / 2 + left
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


"""转换成一次二分搜索"""


class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    # 8:21
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1

        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False