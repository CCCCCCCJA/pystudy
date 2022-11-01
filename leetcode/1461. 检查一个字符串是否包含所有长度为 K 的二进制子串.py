class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        sets = set()
        for i in range(len(s)-k+1):
            tmp = s[i:i+k]
            print(tmp)
            sets.add(tmp)
        if len(sets) == 2 ** k:
            return True
        else:
            return False



s = '00110110'
k = 2
ss = Solution()
print(ss.hasAllCodes(s, k))