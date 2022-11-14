# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        tmp = []
        p = head
        while p:
            tmp.append(p.val)
            p = p.next
        tmp.sort()
        tmp = tmp[::-1]
        q = head
        index = 0
        while q:
            q.val = tmp[index]
            q = q.next
        return head