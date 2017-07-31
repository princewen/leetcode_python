"""

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.

"""

"""
从动态规划的思路出发，我们想从树的底部开始，从下往上累加求和，那么哪种遍历方式可以实现这个要求呢，显然就是后序遍历
在后序遍历的同时，我们用一个dict保存每个求和结果出现的次数，并且记录下出现最多的那个和的次数
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.count = dict()
        self.maxCount = 0

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.postOrder(root)
        res = []
        for i in self.count:
            if self.count[i] == self.maxCount:
                res.append(i)
        return res

    def postOrder(self, root):
        if not root:
            return 0
        left = self.postOrder(root.left)
        right = self.postOrder(root.right)
        sum = left + right + root.val
        self.count[sum] = self.count.get(sum, 0) + 1
        self.maxCount = max(self.maxCount, self.count.get(sum))
        return sum


