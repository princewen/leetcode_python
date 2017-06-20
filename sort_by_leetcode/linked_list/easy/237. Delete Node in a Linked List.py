"""

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.

"""
"""这道题关键是理解题意，不给你整个链表，只给你一个节点，如何把这个节点删除，其实我们没必要真的把这个节点删除，而是把这个节点对应的val值删除即可，所以我们可以偷天换日，
把下一个节点的值赋给这个节点，再把下一个节点删除。
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next