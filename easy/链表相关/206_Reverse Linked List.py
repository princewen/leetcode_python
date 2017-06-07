"""
Reverse a singly linked list.

"""

"""
my solution
两个指针，一个记录当前的头节点，一个记录将要称为头节点的节点
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        p = head
        q = head.next

        while q:
            head.next = q.next
            q.next = p
            p = q
            q = head.next
        return p
