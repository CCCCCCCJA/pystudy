class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 12ms 92%    自己写出来的
        if n == 1 or n == 2:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            for j in range(0, i):
                if dp[j] == 0:
                    dp[i] += dp[i-(j+1)]
                elif dp[i-(j+1)] == 0:
                    dp[i] += dp[j]
                else:
                    dp[i] += dp[j] * dp[i-(j+1)]
        return dp[-1]
