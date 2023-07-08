class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # 76ms 34%
        # maxmax = sum(stones) // 2
        # # value = stones.copy()
        # dp = [0] * (maxmax+1)
        # print(dp)
        # for j in range(len(stones)):
        #     for i in range(len(dp)-1, 0, -1): # 从大往小便利 保证每个石头只添加一次
        #         if i-stones[j] >= 0:
        #             dp[i] = max(dp[i], dp[i-stones[j]]+stones[j])
        #         else:
        #             dp[i] = dp[i]
        #     print(dp)
        # print(dp)
        # return sum(stones) - 2*dp[-1]
        # carl 60ms 85%
        # 到target结束减少循环次数 类似剪枝
        dp = [0] * 15001
        total_sum = sum(stones)
        target = total_sum // 2

        for stone in stones:  # 遍历物品
            for j in range(target, stone - 1, -1):  # 遍历背包
                dp[j] = max(dp[j], dp[j - stone] + stone)

        return total_sum - dp[target] - dp[target]

stones = [31,26,33,21,40]
ss = Solution()
print(ss.lastStoneWeightII(stones))
