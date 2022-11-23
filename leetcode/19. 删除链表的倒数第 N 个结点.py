# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # p = head
        # count = 0
        # while p:
        #     count += 1
        #     p = p.next
        # if count == 1 and n == 1:
        #     return None
        # if count == n:
        #     return head.next
        # q = head
        # for i in range(count - n):
        #     if i == count - n - 1:
        #         q.next = q.next.next
        #         break
        #     q = q.next
        # return head
        # 双指针   没快多少
        p = head
        q = head
        for i in range(n):
            p = p.next
        if p == None:
            return q.next
        while p.next:
            p = p.next
            q = q.next
        q.next = q.next.next
        return head


# head = [1,2,3,4,5], n = 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
n = 2
ss = Solution()
p = ss.removeNthFromEnd(head, n)
while p:
    print(p.val)
    p = p.next