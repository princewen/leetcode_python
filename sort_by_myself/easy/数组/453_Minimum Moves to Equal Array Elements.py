"""

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

"""

"""
solution1: 数组中n-1个数加1，相当于对一个数减1，所以用逆向思维
A move can be interpreted as: "Add 1 to every element and subtract one from any one element". sum(nums_new) = sum(nums) + (n-1): we increment only (n-1) elements by 1.
Visualize the nums array as a bar graph where the value at each index is a bar of height nums[i]. We are looking for minimum moves such that all bars reach the final same height.
Now adding 1 to all the bars in the initial state does not change the initial state - it simply shifts the initial state uniformly by 1.This gives us the insight that a single move is equivalent to subtracting 1 from any one element with respect to the goal of reaching a final state with equal heights.
So our new problem is to find the minimum number of moves to reach a final state where all nums are equal and in each move we subtract 1 from any element.
The final state must be a state where every element is equal to the minimum element. Say we make K moves to reach the final state. Then we have the equation, N * min(nums) = sum(nums) - K.
"""

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums)*len(nums)

"""
同样是上一个思路的思想，不过先对数组进行排序：
Visualize the nums array as a bar graph where the value at each index is a bar of height nums[i]. Sort the array such that the bar at index 0 is minimum height and the bar at index N-1 is highest.
Now in the first iteration, make a sequence of moves such that the height at index 0 is equal to height at index N-1. Clearly this takes nums[N-1]-nums[0] moves. After these moves, index N-2 will be the highest and index 0 will still be the minimum and nums[0] will be same as nums[N-1].
In the next iteration, lets do nums[N-2]-nums[0] moves. After this iteration, nums[0], nums[N-2], and nums[N-1] will be the same.

"""

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        c = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == nums[0]:
                break
            c += nums[i] - nums[0]
        return c

    
"""
暴力方法：
A move can be interpreted as: "Add 1 to every element and subtract one from any one element". sum(nums_new) = sum(nums) + (n-1): we increment only (n-1) elements by 1.
Visualize the nums array as a bar graph where the value at each index is a bar of height nums[i]. We are looking for minimum moves such that all bars reach the final same height.
Now adding 1 to all the bars in the initial state does not change the initial state - it simply shifts the initial state uniformly by 1.This gives us the insight that a single move is equivalent to subtracting 1 from any one element with respect to the goal of reaching a final state with equal heights.
So our new problem is to find the minimum number of moves to reach a final state where all nums are equal and in each move we subtract 1 from any element.
The final state must be a state where every element is equal to the minimum element. Say we make K moves to reach the final state. Then we have the equation, N * min(nums) = sum(nums) - K.
"""

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        while True:
            max1, min1 = max(nums), min(nums)
            if max1 == min1:
                break
            idx, c = nums.index(max1), c+1
            for i in range(len(nums)):
                nums[i] = nums[i] + 1 if i != idx else nums[i]
        return c

"""
改进的暴力方法：
Instead of incrementing by 1 in each iteration, increment in batch. Find the minimum and the maximum. Now we want the minimum to catch up with the maximum. So we perform a batch of moves (maximum - minimum) on all elements except the maximum.
Now after the above step, the minimum would have caught up with the initial maximum and we would have a new maximum now. Repeat this until we have all equal elements.
"""
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        while True:
            max1, min1 = max(nums), min(nums)
            if max1 == min1:
                break
            diff = max1 - min1
            idx, c = nums.index(max1), c + diff
            for i in range(len(nums)):
                nums[i] = nums[i] + diff if i != idx else nums[i]
        return c