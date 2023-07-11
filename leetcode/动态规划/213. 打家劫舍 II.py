class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 16ms 78%
        if len(nums) == 0:  # 如果没有房屋，返回0
            return 0
        if len(nums) == 1:  # 如果只有一个房屋，返回其金额
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        res = []
        nums1 = nums[1:]
        nums2 = nums[:len(nums)-1]
        dp = [0] * (len(nums1))
        dp[0] = nums1[0]
        dp[1] = max(nums1[0], nums1[1])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-2] + nums1[i], dp[i-1])
        res.append(dp[-1])
        dp = [0] * (len(nums2))
        dp[0] = nums2[0]
        dp[1] = max(nums2[0], nums2[1])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-2] + nums2[i], dp[i-1])
        res.append(dp[-1])
        print(res)
        if res[0] > res[1]:
            return res[0]
        else:
            return res[1]





nums = [2,7,9,3,1]
ss = Solution()
ss.rob(nums)