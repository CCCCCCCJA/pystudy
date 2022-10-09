class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head.val == val:
            head = head.next
        p = head
        q = head
        tag = 0
        while p.next:
            if tag > 0:
                q = q.next
            if p.val == val:
                q.next = p.next
            tag += 1
        return head