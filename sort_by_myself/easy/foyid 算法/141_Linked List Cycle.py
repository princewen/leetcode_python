"""

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

"""

"""判断列表中是否有环，只需设置两个指针，一个跑的快，一个跑的慢，当跑的快的追上跑的慢的的时候，肯定就又环，如果碰到next不存在的情况，
抛出异常，肯定没有环
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        walker = head
        runner = head.next
        try:
            while walker != runner:
                walker = walker.next
                runner = runner.next.next
            return True
        except:
            return False