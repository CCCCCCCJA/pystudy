class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum = max(nums)
        for n in nums:
            if n == 0 | n == maxnum:
                continue
            if maxnum < n * 2:
                return -1
        return nums.index(maxnum)


nums = [1,2,16,35,44,100,27,0]
ss = Solution()
print(ss.dominantIndex(nums))
