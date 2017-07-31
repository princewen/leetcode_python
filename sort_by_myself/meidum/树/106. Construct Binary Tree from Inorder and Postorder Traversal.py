"""

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
"""
其实与知道前序和中序求后序的思路一模一样，只不过由前序第一个访问根结点，变成了在后序遍历中最后一个访问根结点，所以大体的思路仍然一样，根据后序遍历结果求根结点，由中序遍历结果确定左右子树的结点，如此递归。

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[0:root_index], postorder[0:root_index])
        root.right = self.buildTree(inorder[root_index + 1:], postorder[root_index:-1])
        return root
