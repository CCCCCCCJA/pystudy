
# 有点问题   没提交成功

class Solution(object):
    def canBeIncreasing(self, nums):
        count = 0
        if len(nums) == 2: return True
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                count += 1
                if count > 1: return False
                if i == 0:
                    continue
                elif nums[i] >= nums[i+2]:
                    return False

        return True

nums = [105,924,32,968]
ss = Solution()
print(ss.canBeIncreasing(nums))