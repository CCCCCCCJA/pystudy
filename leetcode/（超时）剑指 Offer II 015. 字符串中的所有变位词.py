class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        lenp = len(p)
        plist = list(p)
        plist.sort()
        print(plist)
        pstr = ''.join(plist)
        print(pstr)
        wind = lenp
        for i in range(len(s)-lenp+1):
            tmp = s[i:i+wind]
            tmplist = list(tmp)
            tmplist.sort()
            tmpstr = ''.join(tmplist)
            if tmpstr == pstr:
                res.append(i)
        print(res)
        return res


s = 'abab'
p = "ab"
ss = Solution()
ss.findAnagrams(s, p)