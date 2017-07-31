"""

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input: 
         1
       /   \
      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1


"""
"""
递归调用，我们定义了一个辅助函数，函数有两个返回值，一个是子数的所有值的和，另一个是子数的tilt值
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _,ans = self.sumTree(root)
        return ans

    def sumTree(self,node):
        if not node:
            return 0,0
        left,ans1 = self.sumTree(node.left)
        right,ans2 = self.sumTree(node.right)
        return node.val+left+right,abs(right-left)+ans1+ans2