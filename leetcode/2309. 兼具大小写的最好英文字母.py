class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for ss in s:
            if (ord(ss) >= ord('a')) & (ord(ss) <= ord('z')):
                tmp = chr(ord(ss)-32)
                if tmp in s:
                    res.append(ss)
        if len(res) == 0:
            return ''
        print(max(res).upper())
        return max(res).upper()


s = "arRAzFif"
ss = Solution()
ss.greatestLetter(s)