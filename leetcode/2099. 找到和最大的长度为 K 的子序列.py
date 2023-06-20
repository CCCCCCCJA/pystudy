class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        for i in range(len(nums) - k):
            minn = min(nums)
            nums.remove(minn)
        print(nums)
        return nums



nums = [-1,-2,3,4]
k = 3
ss = Solution()
print(ss.maxSubsequence(nums, k))