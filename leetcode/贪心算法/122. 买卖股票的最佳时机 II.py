class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 可同天买卖才行
        res = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                res += prices[i] - prices[i-1]
        print(res)
        return res


prices = [1,2,3,4,5]
ss = Solution()
ss.maxProfit(prices)