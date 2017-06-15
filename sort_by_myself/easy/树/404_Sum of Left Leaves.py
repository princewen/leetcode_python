"""

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

"""

"""my solution
递归的方式，如果数为空，返回0，遍历右子树，随后判断左子树，如果左子树的根结点是叶子结点，则累加该值，否则，继续遍历左子树
"""


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        if root == None:
            return 0

        sum = sum + self.sumOfLeftLeaves(root.right)
        if root.left != None and root.left.left == None and root.left.right == None:
            sum += root.left.val
        else:
            sum += self.sumOfLeftLeaves(root.left)

        return sum

"""same solution"""
class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root: return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)   # isn't leave