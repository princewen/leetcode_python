"""

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

"""
"""先统计链表的数字的个数，然后删除第len-n个数"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        len1 = 0
        while p != None:
            len1 += 1
            p = p.next
        if n == len1:
            return head.next
        else:
            p = head
            len1 = len1 - 1
            while n != len1:
                p = p.next
                len1 = len1 - 1
            p.next = p.next.next
            return head

