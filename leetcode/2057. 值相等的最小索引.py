class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if (i % 10) == nums[i]:
                return i
        return -1

nums = [0, 1, 2]
ss = Solution()
ss.smallestEqual(nums)