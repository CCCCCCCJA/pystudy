class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 8ms 98% myself
        # dp = [0] * (len(nums)+1)
        # dp[1] = nums[0]
        # for i in range(2, len(dp)):
        #     tmp = dp[:i-1]
        #     dp[i] = max(tmp) + nums[i-1]
        # print(dp)
        # return max(dp)
        # carl
        if len(nums) == 0:  # 如果没有房屋，返回0
            return 0
        if len(nums) == 1:  # 如果只有一个房屋，返回其金额
            return nums[0]
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        print(dp)
        print(dp[-1])
        return dp[-1]


nums = [2,7,9,3,1]
ss = Solution()
ss.rob(nums)