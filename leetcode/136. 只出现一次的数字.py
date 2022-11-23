class Solution(object):
    def singleNumber(self, nums):
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res


nums = [2,2,1]
ss = Solution()
print(ss.singleNumber(nums))