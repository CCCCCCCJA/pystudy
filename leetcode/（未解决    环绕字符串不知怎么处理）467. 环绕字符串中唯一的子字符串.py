class Solution(object):
    def findSubstringInWraproundString(self, p):
        s = "abcdefghijklmnopqrstuvwxyz" * 100
        count = 0
        sets = set()
        for i in range(1, len(p)+1):
            for j in range(len(p)-i+1):
                tmp = p[j:j+i]
                if tmp in s:
                    if tmp not in sets:
                        count += 1
                        sets.add(tmp)
        print(count)
        print(sets)
        return count

p = "zab"
ss = Solution()
ss.findSubstringInWraproundString(p)