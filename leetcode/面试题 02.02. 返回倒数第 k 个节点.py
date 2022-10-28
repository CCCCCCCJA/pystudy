# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """
        p = head
        q = head
        for i in range(k):
            p = p.next
        while p:
            p = p.next
            q = q.next
        print(q.val)
        return q.val

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
ss = Solution()
k = 2
ss.kthToLast(head, k)