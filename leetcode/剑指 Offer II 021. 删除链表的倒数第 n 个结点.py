# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        count = 0
        p = head
        while p:
            p = p.next
            count += 1
        if count == n:
            return head.next
        q = head
        for i in range(count-n-1):
            q = q.next
        q.next = q.next.next
        return head