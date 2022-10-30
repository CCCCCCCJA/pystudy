class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res =[]
        listp = list(p)
        listp.sort()
        print(listp)
        lenlen = len(p)
        for i in range(len(s)-lenlen+1):
            tmp = list(s[i:i+lenlen])
            tmp.sort()
            print(tmp)
            tag = 0
            for j in range(len(listp)):
                if tmp[j] != listp[j]:
                    tag = 1
                    break
            if tag == 0:
                res.append(i)
        print(res)
        return res


s = "abab"
p = "ab"
ss = Solution()
ss.findAnagrams(s, p)