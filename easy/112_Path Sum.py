"""

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

"""


"""my solution
使用递归的思想，首先判断节点是否为空，然后判断是否到了叶子节点，如果不是叶子结点，继续往下走
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.left == None and root.right == None:
            return root.val==sum
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
