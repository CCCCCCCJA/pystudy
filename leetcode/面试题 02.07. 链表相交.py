# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p = headA
        q = headB
        len1 = 0
        len2 = 0
        while p:
            len1 += 1
            p = p.next
        while q:
            len2 += 1
            q = q.next
        if p != q:
            return None
        p = headA
        q = headB
        if len1 > len2:
            for i in range(len1-len2):
                p = p.next
            while p != q:
                p = p.next
                q = q.next
            print(p.val)
            return p
        else:
            for i in range(len2-len1):
                q = q.next
            while p != q:
                p = p.next
                q = q.next
            print(q.val)
            return q

listA = ListNode(4)
listA.next = ListNode(1)
listA.next.next = ListNode(8)
listA.next.next.next = ListNode(4)
listA.next.next.next.next = ListNode(5)
listB = ListNode(5)
listB.next = ListNode(6)
listB.next.next = ListNode(1)
listB.next.next.next = ListNode(8)
listB.next.next.next.next = ListNode(4)
listB.next.next.next.next.next = ListNode(5)
