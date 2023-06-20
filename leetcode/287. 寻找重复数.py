class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] ^ nums[i+1] == 0:
                print(nums[i])
                return nums[i]




nums = [3,1,3,4,2]
ss = Solution()
ss.findDuplicate(nums)