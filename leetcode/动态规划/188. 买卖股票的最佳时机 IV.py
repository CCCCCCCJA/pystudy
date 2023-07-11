class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # 96ms 58%
        # 至多买卖k次 可从与买卖股票3推出
        dp = [[0] * (2*k+1) for _ in range(len(prices))]
        for i in range(2*k+1):
            if i % 2 == 0:
                dp[0][i] = 0
            else:
                dp[0][i] = -prices[0]
        for j in dp:
            print(j)
        for i in range(1, len(prices)):
            for j in range(1, 2*k+1):
                if j % 2 == 0:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+prices[i])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]-prices[i])
        # print(dp[-1][2*k])
        return dp[-1][2*k]



k = 2
prices = [3,2,6,5,0,3]
ss = Solution()
ss.maxProfit(k, prices)