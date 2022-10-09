class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        tag = 1
        len_len = len(edges)
        for i in range(1, len_len + 2):
            for e in edges:
                if i not in e:
                    tag = 0
                    break
                else:
                    tag = 1
            if tag == 1:
                return i

edges = [[1,18],[18,2],[3,18],[18,4],[18,5],[6,18],[18,7],[18,8],[18,9],[18,10],[18,11],[12,18],[18,13],[18,14],[15,18],[16,18],[17,18]]
ss = Solution()
print(ss.findCenter(edges))