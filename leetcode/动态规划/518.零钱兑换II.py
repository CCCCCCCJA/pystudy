class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount+1)
        dp[0] = 1
        # 组合
        for i in range(len(coins)): # 物品
            for j in range(coins[i], amount+1): # 背包
                dp[j] += dp[j-coins[i]]
            print(dp)
        # 排列
        # for j in range(amount+1): # 背包
        #     for i in range(len(coins)): # 物品
        #         dp[j] += dp[j-coins[i]]
        #     print(dp)
        # print('-----------------')
        # print(dp)
        return dp[amount]



amount = 5
coins = [1, 2, 5]
ss = Solution()
ss.change(amount, coins)