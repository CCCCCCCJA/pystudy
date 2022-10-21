class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_len = len(nums)
        for i in range(len_len):
            nums[i] = nums[i]**2

        nums.sort()
        print(nums)
        return nums

nums = [-4,-1,0,3,10]
ss = Solution()
ss.sortedSquares(nums)