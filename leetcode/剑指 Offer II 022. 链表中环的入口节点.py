# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = []
        p = head
        while p:
            if p not in tmp:
                tmp.append(p)
                p = p.next
            else:
                print(p)
                return p
        return None


# [3,2,0,-4]
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
ss = Solution()
print(ss.detectCycle(head))