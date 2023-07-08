class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # 1572ms 87%
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # print(dp)
        for str in strs:# 物品
            x = str.count('0')
            y = str.count('1')
            for i in range(n, x-1, -1):
                for j in range(m, y-1, -1): # 背包
                    if i-x >= 0 and j-y >= 0:
                        dp[i][j] = max(dp[i][j], dp[i-x][j-y]+1)
        print(dp[-1][-1]+1)
        return dp[-1][-1]


strs = ["10", "1", "0"]
m = 1
n = 1
ss = Solution()
ss.findMaxForm(strs, m, n)
# for i in range(m, 0, -1):
#     print(i)
