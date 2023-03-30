class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1, -1]
        start = nums.index(target)
        if target == max(nums):
            end = len(nums) - 1
            return [start, end]
        while 1:
            target += 1
            if target in nums:
                end = nums.index(target) - 1
                return [start, end]


nums = [1, 1, 1]
target = 1
ss = Solution()
print(ss.searchRange(nums, target))