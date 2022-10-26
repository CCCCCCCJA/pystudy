class Solution(object):
    def caozuo(self, s):
        tmp = ''
        tmpn = '0'
        for ss in s:
            if (ord(ss) >= 97) & (ord(ss) <= 122):
                tmp += str(ord(ss)-96)
            else:
                tmptmp = int(ss)
                tmpn = str(int(tmpn) + tmptmp)
        # print(tmp, tmpn)
        if len(tmp) != 0:
            return tmp
        else:
            return tmpn
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for i in range(k+1):
            s = self.caozuo(s)
        print(s)
        return int(s)

s = 'iiii'
k = 1
ss = Solution()
ss.getLucky(s, k)