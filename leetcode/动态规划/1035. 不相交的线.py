class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # 96ms 83%
        # 与1143最长公共子序列解法相同
        m = len(nums1) + 1
        print(m)
        n = len(nums2) + 1
        dp = [[0] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                print((i, j))
                if nums1[j-1] == nums2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        print(dp)
        return dp[-1][-1]