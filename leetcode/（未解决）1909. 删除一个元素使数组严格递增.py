
# 有点问题   没提交成功

class Solution(object):
    def canBeIncreasing(self, nums):
        len_len = len(nums)
        count = 0
        for i in range(len_len):
            if i == len_len - 1:
                break
            if nums[i] > nums[i+1]:
                count += 1
            else:
                continue
        if count > 1:
            return False
        else:
            return True

nums = [105,924,32,968]
ss = Solution()
print(ss.canBeIncreasing(nums))