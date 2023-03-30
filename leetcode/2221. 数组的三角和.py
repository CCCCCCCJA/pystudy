class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        while count <= len(nums):
            lenlen = len(nums) - count
            for i in range(lenlen-1):
                nums[i] = (nums[i] + nums[i+1]) % 10
            # nums.pop()
            count += 1
            print(nums)
        return nums[0]


nums = [1,2,3,4,5]
ss = Solution()
ss.triangularSum(nums)