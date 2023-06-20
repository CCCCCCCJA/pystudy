class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            if tmp > res:
                res = tmp
            elif tmp < 0:
                tmp = 0
        print(res)
        return res


nums = [5,4,-1,7,8]
ss = Solution()
ss.maxSubArray(nums)