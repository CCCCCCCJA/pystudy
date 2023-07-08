class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 4ms 100%
        if n == 0 or n == 1:
            return n
        a = 0
        b = 1
        global res
        for i in range(1, n):
            res = a + b
            a = b
            b = res
        # print(res)
        return res