class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 12ms 95%
        # c1 = m-1
        # c2 = n-1
        # tmp = c1 + c2
        # fenzi = 1
        # fenmu = 1
        # for i in range(m-1):
        #     fenzi *= tmp
        #     tmp -= 1
        #     fenmu *= c1
        #     c1 -= 1
        # print(fenzi, fenmu)
        # print(fenzi/fenmu)
        # return fenzi/fenmu
        # dp = [[0]*n]*m
        # carl 动态规划 20ms
        # 创建一个二维列表用于存储唯一路径数
        dp = [[0] * n for _ in range(m)]
        # 设置第一行和第一列的基本情况
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # 计算每个单元格的唯一路径数
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # 返回右下角单元格的唯一路径数
        return dp[m - 1][n - 1]


m = 3
n = 7
sss = Solution()
sss.uniquePaths(m, n)