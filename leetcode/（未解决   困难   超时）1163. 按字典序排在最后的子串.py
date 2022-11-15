class Solution(object):
    def lastSubstring(self, s):
        lenlen = len(s)
        res = []
        for i in range(lenlen):
            for j in range(1, lenlen-i+1):
                tmp = s[i:i+j]
                res.append(tmp)
        res.sort()
        return res[-1]


s = "abab"
ss = Solution()
print(ss.lastSubstring(s))