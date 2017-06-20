"""

Reverse a singly linked list.

"""
"""链表转置，这里实在想不到一个指针的解法了，只能用两个指针，再加上head的帮忙，p指针记录的是每次的队头元素，q指针指向下一个要插入队头的元素"""

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
