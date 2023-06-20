# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        p = list1.next
        pre = list1

        while p:
            if p.val == a:
                resa = pre
            elif p.val == b:
                resb = p.next
                break
            p = p.next
            pre = pre.next
        q = list2
        while q.next:
            q = q.next
        resa.next = list2
        q.next = resb
        return list1


a = 3
b = 4
list2 = [1000000,1000001,1000002]
list1 = ListNode(0)
list1.next = ListNode(1)
list1.next.next = ListNode(2)
list1.next.next.next = ListNode(3)
list1.next.next.next.next = ListNode(4)
list1.next.next.next.next.next = ListNode(5)
list2 = ListNode(1000000)
list2.next = ListNode(1000001)
list2.next.next = ListNode(1000002)
ss = Solution()
res = ss.mergeInBetween(list1, a, b, list2)
p = res
while p:
    print(p.val)
    p = p.next