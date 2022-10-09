class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        node_list = []
        while p:
            if p not in node_list:
                node_list.append(p)
                p = p.next
            else:
                return p