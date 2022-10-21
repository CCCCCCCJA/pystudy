# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res_node = ListNode(0)
        node = res_node
        tag = 0
        p = l1
        q = l2
        while l1 !=None or l2 != None:
            num = p.val + q.val
            if num < 10:
                if tag == 0:
                    node.val = num
                    node = node.next
                else:

            else:

