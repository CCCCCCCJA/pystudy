# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        p = head
        q = head
        res = []
        while p:
            tmp = p.val
            q = q.next
            tag = 0
            while q:
                if q.val > tmp:
                    res.append(q.val)
                    tag = 1
                    break
                q = q.next
            if tag == 0:
                res.append(0)
            p = p.next
            q = p
        print(res)
        return res


head = ListNode(2)
head.next = ListNode(7)
head.next.next = ListNode(4)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)
ss = Solution()
ss.nextLargerNodes(head)