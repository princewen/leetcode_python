"""

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

"""

"""
my solution 递归的思想
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if not root:
            return res
        if not root.left and not root.right:
            return [str(root.val)]

        leftPath = self.binaryTreePaths(root.left)
        rightPath = self.binaryTreePaths(root.right)
        for item in leftPath:
            res.append("->".join([str(root.val), item]))
        for item in rightPath:
            res.append("->".join([str(root.val), item]))
        return res
