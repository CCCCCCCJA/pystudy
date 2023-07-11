class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[i][0]持有股票的最大金额
        # dp[i][1]不持有股票的最大金额
        a = -prices[0]
        b = 0
        # print(dp)
        for i in range(1, len(prices)):
            a = max(a, b-prices[i])
            b = max(b, a + prices[i])
        # print(dp)
        return b