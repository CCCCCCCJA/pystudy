# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            return head
        p = head
        k = head.next
        m = None
        count = 0
        while p is not None:
            if count > 0:
                q = p.next
                if q is None:
                    return k
                p.next = q.next
                q.next = p
                m.next = q
            else:

                q = p.next
                if q is None:
                    return k
                p.next = q.next
                q.next = p
            count += 1
            m = p
            p = p.next
        return k




