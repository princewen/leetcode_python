"""

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

"""

"""
AVL tree 是一种特殊的二叉查找树，，首先我们要在树中引入平衡因子balance，
表示结点右子树的高度减去左子树的高度差（右-左），对于一棵AVL树要么它是一棵空树，
要么它是一棵高度平衡的二叉查找树，平衡因子balance绝对值不超过1
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root