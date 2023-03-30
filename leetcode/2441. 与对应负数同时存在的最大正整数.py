class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -1
        for i in range(len(nums)):
            if nums[i] > 0:
                if -nums[i] in nums and nums[i] > res:
                    res = nums[i]
        print(res)
        return res
    # 双指针更快


nums = [-1, 2, -3, 3]
ss = Solution()
ss.findMaxK(nums)