"""

A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.


"""
"""假如长度为5，并不是组合数c53，而是1+2+3，所以就用动态规划的思路进行求解，用一个数组保存到当前位置时满足条件的子数组的个数"""
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        opt,i= [0,0],1
        for j in range(2,len(A)):
            if A[j] - A[j-1] == A[j-1] - A[j-2]:
                opt.append(opt[j-1]+i)
                i+=1
            else:
                opt.append(opt[j-1])
                i = 1
        return opt[-1]