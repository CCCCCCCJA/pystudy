class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 12ms 93%
        if n == 0:
            return 1
        if n == 1:
            return 2
        a = 1
        b = 2
        global res
        for i in range(n-2):
            res = a + b
            a = b
            b = res
        # print(res)
        return res
