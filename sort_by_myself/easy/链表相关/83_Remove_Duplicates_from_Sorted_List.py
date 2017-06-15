"""

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

"""

"""my solution"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = head
        cur = head.next
        dummy.next = None

        while cur:
            if cur.val == dummy.val:
                cur = cur.next
            else:
                dummy.next = cur
                dummy = cur
                cur = cur.next
                dummy.next = None
        return head

"""other solution"""

def deleteDuplicates(self, head):
    cur = head
    while cur:
        while cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next     # skip duplicated node
        cur = cur.next     # not duplicate of current node, move to next node
    return head