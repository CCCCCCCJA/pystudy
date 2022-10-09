# 内存超了
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        for i in range(k):
            p = head
            q = head
            tag = 0
            while(p.next != None):
                if(tag > 0):
                    q = q.next
                p = p.next
                tag += 1
            p.next = head
            head = p
            q.next = None
        return head

# class Solution:
#     def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if head == None: return None
#         temp = head
#         n = 1
#         while temp.next:
#             temp = temp.next
#             n += 1
#         temp.next = head
#         for i in range(n-k%n):
#             temp = temp.next
#         head = temp.next
#         temp.next = None
#         return head


