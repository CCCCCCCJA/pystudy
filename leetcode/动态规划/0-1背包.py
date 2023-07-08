class Solution(object):
    def zeroonebag(self, weight, value, maxmax):
        dp = [[0] * (maxmax+1) for _ in range(len(value))]
        print(dp)
        for i in range(len(dp[0])):
            if i >= weight[0]:
                dp[0][i] = value[0]
        print(dp)
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if j-weight[i] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
        print(dp)



value = [15, 20 ,30]
weight = [1, 3, 4]
ss = Solution()
ss.zeroonebag(weight, value, 4)

