class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i]为以nums[i]结尾的最长递增子序列
        # 1976ms 45%
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)




nums = [0,1,0,3,2,3]
ss = Solution()
print(ss.lengthOfLIS(nums))
