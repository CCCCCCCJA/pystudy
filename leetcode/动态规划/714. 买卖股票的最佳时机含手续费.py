class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # 182ms 87%
        a = -prices[0]
        b = 0
        # print(dp)
        for i in range(1, len(prices)):
            a = max(a, b-prices[i])
            b = max(b, a + prices[i]-fee)  # 这里与买卖股票2不同
        # print(dp)
        return b


prices = [1,3,2,8,4,9]
fee = 2
ss = Solution()
print(ss.maxProfit(prices, fee))
