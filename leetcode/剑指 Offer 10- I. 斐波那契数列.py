class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # F = [0, 1]
        # if n == 0:
        #     return F[0]
        # if n == 1:
        #     return F[1]
        # for i in range(2, n+1):
        #     F.append(F[i-1]+F[i-2])
        # print(F)
        # print(F[n])
        # return F[n]
        a = 0
        b = 1
        sum = 0
        for i in range(2, n+1):
            sum = (a+b) % (10**9+7)
            a = b
            b = sum
        return b


n = 5
ss = Solution()
print(ss.fib(n))