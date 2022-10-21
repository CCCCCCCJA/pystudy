# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head != None:
            p = head.next
        else:
            return head
        q = head
        while p:
            if p.val == q.val:
                q.next = p.next
                p.next = None
                p = q
            else:
                q = q.next
            p = p.next
        return head
