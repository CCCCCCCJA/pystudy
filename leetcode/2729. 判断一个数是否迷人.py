class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = str(n) + str(2*n) + str(3*n)
        print(res)
        if '0' in res:
            return False
        for i in range(1, 10):
            if res.count(str(i)) != 1:
                return False
            else:
                return True


n = 192
ss = Solution()
ss.isFascinating(n)