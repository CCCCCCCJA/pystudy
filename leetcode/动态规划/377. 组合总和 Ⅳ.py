class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # 20ms 80%
        dp = [0] * (target+1)
        dp[0] = 1
        # 排列
        for j in range(target+1): # 背包
            for i in range(len(nums)): # 物品
                if j-nums[i] >= 0:
                    dp[j] += dp[j-nums[i]]
            print(dp)
        print('-----------------')
        print(dp)
        return dp[target]



nums = [1,2,3]
target = 4
ss = Solution()
ss.combinationSum4(nums, target)