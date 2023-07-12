class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # dp[i][j]以i-1为结尾的nums1和以j-1为结尾的nums2的最长重复子数组
        m = len(nums1) + 1
        n = len(nums2) + 1
        dp = [[0] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                if nums2[i-1] == nums1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
        print(dp)
        res = max([item for dp1 in dp for item in dp1])
        print(res)
        return res




nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4]
ss = Solution()
ss.findLength(nums1, nums2)