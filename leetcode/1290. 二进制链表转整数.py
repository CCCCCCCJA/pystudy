# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        p = head
        res = []
        while p:
            res.append(p.val)
            p = p.next
        res = res[::-1]
        resInt = 0
        for i in range(len(res)):
            if res[i] == 1:
                resInt += 2 ** i
        print(resInt)
        return resInt


head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)
ss = Solution()
ss.getDecimalValue(head)