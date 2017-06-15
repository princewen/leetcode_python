"""

You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]

"""

"""我的解法是：定义一个字典保存每一行的所有值，使用深度优先遍历对数进行遍历，同时遍历的时候保存行号
append方法不返回新的数组，直接在原数组的基础上改，返回none，所以使用+号对数组进行连接
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        rows = dict()
        stack = []
        stack.append([root, 0])
        rows[0] = rows.get(0, []) + [root.val]
        while stack != []:
            topnode = stack.pop()
            if topnode[0].right != None:
                stack.append([topnode[0].right, topnode[1] + 1])
                rows[topnode[1] + 1] = rows.get(topnode[1] + 1, []) + [topnode[0].right.val]
            if topnode[0].left != None:
                stack.append([topnode[0].left, topnode[1] + 1])
                rows[topnode[1] + 1] = rows.get(topnode[1] + 1, []) + [topnode[0].left.val]
        return [max(rows[t]) for t in range(len(rows.keys()))]

"""更简单的想法，直接遍历每一层"""
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        maxs = []
        row = [root]
        while any(row):
            maxs.append(max(node.val for node in row))
            row = [kid for node in row for kid in (node.left,node.right) if kid]
        return maxs

