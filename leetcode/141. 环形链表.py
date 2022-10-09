class Solution(object):
    def hasCycle(self, head):
        p = head
        list = []
        while p:
            if p not in list:
                list.append(p)
                p = p.next
            else:
                return True
        return False