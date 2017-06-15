"""

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

"""
"""思想，主要是递归遍历，我一开始想的是如果节点值等于待求和值，数量加1，然后向左字数遍历，求和值有原值和原值-节点值，但是这样递归的话不连续的
节点也可能和等于待求和值，造成结果多了很多，新的思路不会出现中断的情况，其余思路相似。
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.pathSumFrom(root,sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)
    def pathSumFrom(self,node,sum):
        if not node:
            return 0
        return (1 if node.val==sum else 0) + self.pathSumFrom(node.left,sum-node.val)+self.pathSumFrom(node.right,sum - node.val)