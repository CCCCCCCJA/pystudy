class Solution(object):
    def isUnique(self, astr):
        a = ''
        for s in astr:
            if s in a:
                return False
            else:
                a += s
        return True

s = "leetcode"
ss = Solution()
print(ss.isUnique(s))