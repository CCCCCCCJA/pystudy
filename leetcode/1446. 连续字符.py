class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxn = 1
        tmp = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                tmp += 1
            else:
                if tmp > maxn:
                    maxn = tmp
                tmp = 1
        print(maxn)
        return maxn


s = "abbcccddddeeeeedcba"
ss = Solution()
ss.maxPower(s)
