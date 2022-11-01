# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 执行用时：64ms, 在所有Python提交中击败了97.66 %的用户
        tmp = []
        for i in range(len(lists)):
            head = lists[i]
            while head:
                tmp.append(head.val)
                head = head.next
        tmp.sort()
        p= ListNode(tmp[0])
        q = p
        for i in range(1, len(tmp)):
            p.next = ListNode(tmp[i])
            p = p.next
        return q