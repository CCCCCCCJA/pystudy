class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # dp[i][j] 从(0, i-1]nums1和以(0, j-1]的最长公共子序列长度为dp[i][j]
        # 516ms 83%
        m = len(text1) + 1
        print(m)
        n = len(text2) + 1
        dp = [[0] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                print((i, j))
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        print(dp)
        return dp[-1][-1]


text1 = "abcde"
text2 = "ace"
ss = Solution()
ss.longestCommonSubsequence(text1, text2)