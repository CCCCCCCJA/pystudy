class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -101
        maxn = max(nums)
        for i in range(1, len(nums)):
            tmp = nums[i] * nums[i-1]
            if tmp > res:
                res = tmp
        # print(res)
        if maxn > res:
            res = maxn
        return res


nums = [-3, -4]
ss = Solution()
print(ss.maxProduct(nums))