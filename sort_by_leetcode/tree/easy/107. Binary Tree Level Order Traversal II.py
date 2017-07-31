"""

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]


"""

"""
这里我们采用深度优先遍历的方式得到结果的输出：

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = [(root,0)]
        res = []
        while stack!=[]:
            node,level = stack.pop()
            if node:
                if len(res) < (level+1):
                    res.insert(0,[])
                res[-(level+1)].append(node.val)
                stack.append((node.right,level+1))
                stack.append((node.left,level+1))
        return res