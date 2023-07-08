class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 12ms 97%
        # 没怎么听懂
        dp = [0] * (n+1)
        print(len(dp))
        # dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(i+1):
                dp[i] = max(dp[i], j * (i-j), j * dp[i-j])
        print(dp)
        return dp[-1]


ss = Solution()
ss.integerBreak(10)