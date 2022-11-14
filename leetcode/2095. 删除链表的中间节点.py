# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        # 执行用时：2076ms, 在所有Python提交中击败了26.09 %的用户
        # p = head
        # q = head
        # s = head
        # while p and p.next:
        #     p = p.next.next
        #     q = q.next
        # while s:
        #     if s.next == q:
        #         s.next = s.next.next
        #     s = s.next
        # return head
        if head.next is None:
            return None
        slow, fast, pre = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        pre.next = pre.next.next
        return head