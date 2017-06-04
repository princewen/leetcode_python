"""

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

"""

"""my solution
采用中序遍历的方式
"""

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

        if p != None and q != None:
            if self.isSameTree(p.left, q.left) and p.val == q.val and self.isSameTree(p.right, q.right):
                return True
            else:
                return False
        else:
            if p == None and q == None:
                return True
            else:
                return False


"""more simple way"""
def isSameTree(self, p, q):
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    return p is q