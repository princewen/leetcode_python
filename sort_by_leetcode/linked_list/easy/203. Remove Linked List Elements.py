"""

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

"""
"""有了第83题的思路，我们这里可以用一个指针来进行链表的遍历，但是这里需要注意的是，头节点也需要进行判断，如果头节点的值等于val的话，我们不能返回头节点，所以这里很巧妙的重新生成了一个无关的头节点"""

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
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while cur:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
            cur=cur.next
        return dummy.next