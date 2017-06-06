"""

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

"""
"""
my solution
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        while head and head.val==val:
            head = head.next
        if not head:
            return None
        p = head.next
        q = head
        while p:
            if p.val == val:
                q.next = p.next
                p = p.next
            else:
                q = p
                p = p.next
        return head