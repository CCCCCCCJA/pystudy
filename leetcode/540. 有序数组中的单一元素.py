class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for ns in nums:
            res ^= ns
        print(res)
        return res
    # 使用二分算法的时间复杂度为logn


nums = [1,1,2,3,3,4,4,8,8]
ss = Solution()
ss.singleNonDuplicate(nums)