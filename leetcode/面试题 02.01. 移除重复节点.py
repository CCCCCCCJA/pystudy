# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmpSet = set()
        p = head
        if p == None or p.next == None:
            return head
        q = head.next
        tmpSet.add(p.val)
        while q:
            if q.val in tmpSet:
                p.next = q.next
                q = p.next
            else:
                tmpSet.add(q.val)
                p = p.next
                q = q.next
        x = head
        while x:
            print(x.val)
            x = x.next
        return head


# [1, 2, 3, 3, 2, 1]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(2)
head.next.next.next.next.next = ListNode(1)
ss = Solution()
ss.removeDuplicateNodes(head)