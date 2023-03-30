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
        # resSet = set()
        # for i in range(len(s)):
        #     for j in range(len(s)-i):
        #         resSet.add(s[j:j+i+1])
        # resList = list(resSet)
        # resList.sort()
        # print(resList[-1])
        # return resList[-1]

s = "abab"
ss = Solution()
print(ss.lastSubstring(s))