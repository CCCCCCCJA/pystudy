class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[i][0] 持有股票的状态
        # dp[i][1] 保持卖出股票的状态
        # dp[i][2] 卖出股票状态
        # dp[i][3] 冷冻期
        # 将不持有股票的状态拆分为三部分 保持卖出股票的状态、卖出股票状态、冷冻期状态
        # 24ms 44%
        dp = [[0] * 4 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0
        dp[0][3] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][3]-prices[i], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][3])
            dp[i][2] = dp[i-1][0] + prices[i]
            dp[i][3] = dp[i-1][2]
        print(dp[-1][2])
        return max(dp[-1][2], dp[-1][1], dp[-1][3])