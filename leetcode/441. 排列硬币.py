class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        layer = 0
        i = 1
        while 1:
            if n - i >= 0:
                layer += 1
                n -= i
                i += 1
            else:
                return layer



n = 5
ss = Solution()
print(ss.arrangeCoins(n))