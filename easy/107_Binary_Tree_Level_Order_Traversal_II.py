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
import collections
"""solution1 : stack + dfs
利用栈来进行存储深度优先搜索需要遍历的节点，注意压入栈的时候要先压入右节点，再压入左节点
这样才能做到先访问左节点
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

"""solution2 利用队列

"""

def levelOrderBottom(self, root):
    queue, res = collections.deque([(root, 0)]), []
    while queue:
        node, level = queue.popleft()
        if node:
            if len(res) < level+1:
                res.insert(0, [])
            res[-(level+1)].append(node.val)
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
    return res