# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        tmp = []
        p = list1
        while p:
            tmp.append(p.val)
            p = p.next
        q = list2
        while q:
            tmp.append(q.val)
            q = q.next
        tmp.sort()
        res = ListNode(tmp[0])
        resres = res
        for i in range(1, len(tmp)):
            tmptmp = ListNode(tmp[i])
            res.next = tmptmp
            res = res.next
        return resres

