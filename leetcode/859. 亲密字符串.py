# 时间超了

class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        res = list(s)
        result = ''
        if(s == goal): return True
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                res = list(s)
                tmp = res[i]
                res[i] = res[j]
                res[j] = tmp
                for r in res:
                    result += r
                if(result == goal):
                    return True
                result = ''
        return False

s = "aabc"

goal = "aacb"
ss = Solution()
print(ss.buddyStrings(s, goal))