"""
Given a singly linked list, determine if it is a palindrome.
"""
"""
画图理解更好，使用两个指针，当快的指针跑到头的时候，跑的慢的指针刚好到一半，随后将后一半元素的指向改变，随后循环判断元素是否相等
相当于先把一个链表分成两个
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt

        while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
