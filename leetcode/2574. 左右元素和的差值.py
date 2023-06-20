class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            leftSum = sum(nums[0:i])
            rightSum = sum(nums[i+1:])
            # print(leftSum, rightSum, abs(leftSum-rightSum))
            res.append(abs(leftSum-rightSum))
        return res


nums = [10,4,8,3]
ss = Solution()
ss.leftRightDifference(nums)