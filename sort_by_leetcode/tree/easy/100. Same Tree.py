"""

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

"""
"""递归的判断两个数是否相等，并判断两棵树时候同时为空，即结构是否相等"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            if p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
                return True
            else:
                return False
        return p is q