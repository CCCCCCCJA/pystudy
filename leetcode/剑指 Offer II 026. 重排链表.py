# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        tmpp = head
        count = 1
        while tmpp.next != None:
            count += 1
            rep = tmpp
            tmpp = tmpp.next
        tag = 0
        for i in range(int(count >> 1)):
            if tag == 0:
                p = head
                for j in range(i*2):
                    p = p.next
                tag = 1
                rep.next = None
                tmp = p.next
                p.next = tmpp
                tmpp.next = tmp
                continue
            tmpp1 = head
            while tmpp1.next != None:
                rep = tmpp1
                tmpp1 = tmpp1.next
            p1 = head
            for j in range(i * 2):
                p1 = p1.next
            rep.next = None
            tmp = p1.next
            p1.next = tmpp1
            tmpp1.next = tmp
        # p = head
        # while p:
        #     print(p.val)
        #     p = p.next
        return head



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
ss = Solution()
ss.reorderList(head)