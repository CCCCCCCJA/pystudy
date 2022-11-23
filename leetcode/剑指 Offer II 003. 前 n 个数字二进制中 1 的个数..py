class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(n+1):
            tmpstr = bin(i).replace('0b', '')
            res.append(tmpstr.count('1'))
        print(res)
        return res


n = 2
ss = Solution()
ss.countBits(n)