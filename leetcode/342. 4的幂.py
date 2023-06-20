class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        res = int(n ** 0.25)
        print(res)
        if 4 ** res == n:
            return True
        else:
            return False




n = 4
ss = Solution()
ss.isPowerOfFour(n)