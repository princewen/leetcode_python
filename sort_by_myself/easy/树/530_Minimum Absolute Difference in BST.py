"""

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

"""
"""mysolution:中序遍历二叉搜索树得到的结果是排好序的，所以先对树进行非递归的中序遍历，随后再找最小差异值"""


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        nums = []
        stack = []
        p = root
        while p:
            stack.append(p)
            p = p.left
        while stack != []:
            p = stack.pop()
            nums.append(p.val)
            p = p.right
            while p:
                stack.append(p)
                p = p.left

        min = 0xffffffff
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] < min:
                min = nums[i + 1] - nums[i]
        return min
