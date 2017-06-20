"""

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

"""
"""
判断一个链表是否是回文的，很自然的想法就是两个指针，一个指针从前往后走，一个指针从后往前走，判断元素值是否相同，这里要分几个步骤来进行求解：
1、找到链表长度的一半，用追赶法，一个指针一次走两步，一个指针一次走一步
2、将后一半数组转置
3、判断链表是否是回文链表
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
