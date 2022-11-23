class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        res = []
        lenlen = len(nums)
        for i in range(lenlen):
            sumn = sum(nums[i+1:]) - nums[i] * (lenlen-i-1)
            for j in range(i):
                sumn += nums[i] - nums[j]
            res.append(sumn)
        print(res)
        return res

nums = [2,3,5]
ss = Solution()
ss.getSumAbsoluteDifferences(nums)