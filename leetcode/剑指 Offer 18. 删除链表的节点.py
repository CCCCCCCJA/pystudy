# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = head
        q = head
        if p.val != val:
            p = p.next
        else:
            return head.next
        while p:
            if p.val == val:
                q.next = q.next.next
                return head