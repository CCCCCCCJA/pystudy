class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 680ms 85%
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for cs in coins:
            for j in range(cs, amount+1):
                if dp[j - cs] != float('inf'):
                    dp[j] = min(dp[j], dp[j-cs]+1)
            print(dp)
        print('---------------')
        print(dp)
        print(dp[-1])
        return dp[amount]




coins = [1, 2, 5]
amount = 11
ss = Solution()
ss.coinChange(coins, amount)