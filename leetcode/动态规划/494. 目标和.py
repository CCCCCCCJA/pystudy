class Solution:
    # 一维 二维没弄明白
    def findTargetSumWays(self, nums, target):
        # 二维dp数组
        total_sum = sum(nums)  # 计算nums的总和
        if abs(target) > total_sum:
            return 0  # 此时没有方案
        if (target + total_sum) % 2 == 1:
            return 0  # 此时没有方案
        target_sum = (target + total_sum) // 2  # 目标和
        # 创建二维动态规划数组，行表示选取的元素数量，列表示累加和
        dp = [[0] * (target_sum + 1) for _ in range(len(nums) + 1)]
        # 初始化状态
        dp[0][0] = 1
        # 动态规划过程
        for i in range(1, len(nums) + 1):
            for j in range(target_sum + 1):
                dp[i][j] = dp[i - 1][j]  # 不选取当前元素
                if j >= nums[i - 1]:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]  # 选取当前元素
        # return dp[len(nums)][target_sum]  # 返回达到目标和的方案数
        for i in dp:
            print(i)
        print('-----------------------')
        # 一维dp数组
        # total_sum = sum(nums)  # 计算nums的总和
        # if abs(target) > total_sum:
        #     return 0  # 此时没有方案
        # if (target + total_sum) % 2 == 1:
        #     return 0  # 此时没有方案
        # target_sum = (target + total_sum) // 2  # 目标和
        # dp = [0] * (target_sum + 1)  # 创建动态规划数组，初始化为0
        # dp[0] = 1  # 当目标和为0时，只有一种方案，即什么都不选
        # for num in nums:
        #     for j in range(target_sum, num - 1, -1):
        #         dp[j] += dp[j - num]  # 状态转移方程，累加不同选择方式的数量
        #     print(dp)
        # return dp[target_sum]  # 返回达到目标和的方案数


nums = [1, 1, 1, 1, 1]
target = 3
ss = Solution()
print(ss.findTargetSumWays(nums, target))
