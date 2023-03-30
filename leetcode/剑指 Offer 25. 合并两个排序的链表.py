# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(-1)
        m = res
        p = l1
        q = l2
        while p and q:
            if p.val <= q.val:
                tmp = ListNode(p.val)
                m.next = tmp
                p = p.next
                m = m.next
            else:
                tmp = ListNode(q.val)
                m.next = tmp
                q = q.next
                m = m.next
        if p:
            m.next = p
            return res.next
        if q:
            m.next = q
            return res.next
        return res.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
ss = Solution()
res = ss.mergeTwoLists(l1, l2)
while res:
    print(res.val)
    res = res.next



