"""

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

"""

"""移动的目标元素是排序后数组的中间位置
考虑数组数量是偶数个：中间的元素选哪个都可以，考虑[2，3，8，10],3和8的差距是5，如果选择都变成3，那么10变成3比10变成8多变了5，
如果选择了8，2变到8比变到3多变了5次，其他元素也可以这么考虑，所以选哪一个都可以
如果数组元素是奇数个：则选择中间那个元素。
"""

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        median = sorted(nums)[len(nums) / 2]
        return sum(abs(num - median) for num in nums)
