# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        countA = 0
        countB = 0
        p = headA
        q = headB
        while p.next:
            p = p.next
            countA += 1
        while q.next:
            q = q.next
            countB += 1
        if q != p:
            return None
        k = headA
        m = headB
        if countA >= countB:
            for i in range(countA-countB):
                k = k.next
            while k and m:
                if k.val == m.val:
                    return k
                k = k.next
                m = m.next
        else:
            for i in range(countB-countA):
                k = k.next
            while k and m:
                if k.val == m.val:
                    return k
                k = k.next
                m = m.next