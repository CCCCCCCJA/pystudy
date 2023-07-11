class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[i][0]持有股票的最大金额
        # dp[i][1]不持有股票的最大金额
        # 只可以买卖一次
        # 472ms
        # dp = [[0, 0] for _ in range(len(prices))]
        #
        # dp[0][0] = -prices[0]
        # dp[0][1] = 0
        # print(dp)
        # for i in range(1, len(prices)):
        #     dp[i][0] = max(dp[i-1][0], -prices[i])
        #     dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        # print(dp)
        # return max(dp[-1][0], dp[-1][1])
        # 240ms 43%
        a = -prices[0]
        b = 0
        # print(dp)
        for i in range(1, len(prices)):
            a = max(a, -prices[i])
            b = max(b, a + prices[i])
        # print(dp)
        return  b


prices = [7,1,5,3,6,4]
ss = Solution()
ss.maxProfit(prices)