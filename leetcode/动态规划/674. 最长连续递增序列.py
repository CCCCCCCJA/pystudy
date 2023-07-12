class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 16ms 94%
        # dp[i]为以nums[i]结尾的最长连续递增序列
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
        return max(dp)


nums = [2,2,2,2,2]
ss = Solution()
print(ss.findLengthOfLCIS(nums))