"""

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


"""

"""my solution 递归的方式"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            leftmax = self.maxDepth(root.left)+1
            rightmax = self.maxDepth(root.right)+1
            return max(leftmax,rightmax)

"""other solution
将我的思想转化为一行，巧妙利用了map函数
"""

def maxDepth(self, root):
    return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0

