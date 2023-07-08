class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 20ms 79%
        # dp = [0] * (len(cost) + 1)
        a = 0
        b = 0
        global res
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
            res = min(a + cost[i - 1], b + cost[i - 2])
            a = b
            b = res
        # print(dp)
        return res


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
ss = Solution()
print(ss.minCostClimbingStairs(cost))
