# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = l1
        q = l2
        l1List = []
        l2List = []
        while p:
            l1List.append(p)
            p = p.next
        while q:
            l2List.append(q)
            q = q.next
        r1 = len(l1List) - 1
        r2 = len(l2List) - 1
        res = []
        if r1 >= r2:
            tag = 0
            for i in range(r2+1):
                tmpsum = l1List[r1].val + l2List[r2].val + tag
                if tmpsum >= 10:
                    tag = 1
                    res.append(tmpsum % 10)
                else:
                    tag = 0
                    res.append(tmpsum)
                r1 -= 1
                r2 -= 1
            print(r1, r2, tag)
            if r1 >= 0:
                while r1 >= 0:
                    tmpsum = l1List[r1].val + tag
                    if tmpsum >= 10:
                        tag = 1
                        res.append(tmpsum % 10)
                    else:
                        tag = 0
                        res.append(tmpsum)
                    r1 -= 1
                if tag == 1:
                    res.append(1)
        else:
            tag = 0
            for i in range(r1+1):
                tmpsum = l1List[r1].val + l2List[r2].val + tag
                if tmpsum >= 10:
                    tag = 1
                    res.append(tmpsum % 10)
                else:
                    tag = 0
                    res.append(tmpsum)
                r1 -= 1
                r2 -= 1
            print(r1, r2, tag)
            if r2 >= 0:
                while r2 >= 0:
                    tmpsum = l1List[r2].val + tag
                    if tmpsum >= 10:
                        tag = 1
                        res.append(tmpsum % 10)
                    else:
                        tag = 0
                        res.append(tmpsum)
                    r2 -= 1
                if tag == 1:
                    res.append(1)
        res = res[::-1]
        print(res)
        head = ListNode(res[0])
        p = head
        for i in range(1, len(res)):
            p.next = ListNode(res[i])
            p = p.next
        return head


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
# l1.next.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
ss = Solution()
ss.addTwoNumbers(l1, l2)

