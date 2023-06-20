# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        p = head
        res = ListNode(0)
        q = res
        tmp = []
        while p:
            print(p.val)
            if p.next == None:
                print(tmp)
                if p.val not in tmp:
                    q.next = ListNode(p.val)
                    q = q.next
                    break
                else:
                    break
            if p.val != p.next.val and p.val not in tmp:
                q.next = ListNode(p.val)
                q = q.next
                p = p.next
            else:
                tmp.append(p.val)
                p = p.next
        return res.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)
ss = Solution()
res = ss.deleteDuplicates(head)
while res:
    print(res.val)
    if res.next != None:
        res = res.next
    else:
        break

