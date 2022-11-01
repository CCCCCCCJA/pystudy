class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = [1, n]
        for i in range(2, n):
            if n / i == int(n / i):
                res.append(i)
            if len(res) > 3:
                return False
        if len(res) == 3:
            return True
        else:
            return False

n = 4
ss = Solution()
ss.isThree(n)