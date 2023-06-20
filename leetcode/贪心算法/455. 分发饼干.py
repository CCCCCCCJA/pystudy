class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count = 0
        index = len(s) - 1
        for i in range(len(g) - 1, -1, -1):

            while index >= 0 and s[index] >= g[i]:
                count += 1
                index -= 1
                break
        # print(count)
        return count



g = [1,2,7,10]
s = [1,3,5,9]
ss = Solution()
ss.findContentChildren(g, s)