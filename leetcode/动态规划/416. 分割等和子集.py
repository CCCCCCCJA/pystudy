class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 == 0:
            maxmax = sum(nums) // 2
        else:
            return False
        value = nums.copy()
        dp = [0] * (maxmax+1)
        print(dp)
        for j in range(len(nums)): # 物品
            for i in range(len(dp)-1, 0, -1): # 背包     # 从大往小便利 保证每个石头只添加一次
                if i-nums[j] >= 0:
                    dp[i] = max(dp[i], dp[i-nums[j]]+value[j])
                else:
                    dp[i] = dp[i]
            print(dp)
        print(dp)
        if dp[-1] == maxmax:
            return True
        else:
            return False


nums = [1,2,5]
ss = Solution()
print(ss.canPartition(nums))