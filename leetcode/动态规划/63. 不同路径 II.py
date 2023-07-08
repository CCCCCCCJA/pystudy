class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 16ms 81%
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        dp = [[0] * n for _ in range(m)]
        print(dp, m , n)
        print(obstacleGrid)
        # 设置第一行和第一列的基本情况
        for i in range(m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = 1
            else:
                break
        # 计算每个单元格的唯一路径数
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


obstacleGrid = [[1, 0]]
ss = Solution()
print(ss.uniquePathsWithObstacles(obstacleGrid))