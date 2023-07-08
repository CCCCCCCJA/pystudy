class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        realSum = (n * (n + 1)) // 2
        xSum = sum(nums)
        if xSum - realSum == 0:
            return 0
        else:
            return realSum - xSum

nums = [0,1,3]
ss = Solution()
ss.missingNumber(nums)